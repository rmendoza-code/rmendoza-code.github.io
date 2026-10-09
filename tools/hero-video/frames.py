import sys
from PIL import Image, ImageDraw, ImageFilter
R,S=sys.argv[1],sys.argv[2]; W,H=1920,1080; TOP=110; CX=1300
def bg():
    im=Image.new('RGB',(W,H),(17,18,20)); g=Image.new('L',(W,H),0)
    ImageDraw.Draw(g).ellipse((CX-700,-90,CX+700,1210),fill=60)
    im.paste(Image.new('RGB',(W,H),(42,44,50)),(0,0),g.filter(ImageFilter.GaussianBlur(220))); return im
def place(fig,scale,out):
    f=fig.resize((int(fig.width*scale),int(fig.height*scale)),Image.LANCZOS)
    f=f.crop((0,0,f.width,H-TOP)); im=bg(); im.paste(f,(CX-f.width//2,TOP),f); im.save(out)
wave=Image.open(R+'/assets/site/img/wave.webp').convert('RGBA'); sw=970/1319*0.95
hero=Image.open(R+'/assets/site/img/hero.webp').convert('RGBA'); sh=970/1770*1.0
place(hero,sh,S+'/start.png'); place(wave,sw,S+'/end.png')
a=Image.open(S+'/start.png');b=Image.open(S+'/end.png')
c=Image.blend(a,b,0.5); c.resize((960,540)).save(S+'/blend.png')
