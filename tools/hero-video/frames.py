import sys
from PIL import Image, ImageDraw, ImageFilter
R,S=sys.argv[1],sys.argv[2]; W,H=1920,1080; TOP=110; CX=1300
PAL={ # base, glow (behind figure), edge (vignette)
 'cobalto':((59,79,224),(110,128,255),(30,42,150)),
 'azul-noche':((18,28,92),(59,79,224),(8,12,48)),
 'lima':((184,224,140),(222,245,190),(140,190,100)),
 'amarillo-neon':((228,255,58),(246,255,170),(190,220,20)),
}
def bg(base,glow,edge):
    im=Image.new('RGB',(W,H),base)
    g=Image.new('L',(W,H),0); ImageDraw.Draw(g).ellipse((CX-650,-60,CX+650,1180),fill=255)
    im.paste(Image.new('RGB',(W,H),glow),(0,0),g.filter(ImageFilter.GaussianBlur(260)))
    v=Image.new('L',(W,H),255); ImageDraw.Draw(v).ellipse((-300,-350,W+300,H+350),fill=0)
    im.paste(Image.new('RGB',(W,H),edge),(0,0),v.filter(ImageFilter.GaussianBlur(200)))
    return im
def place(fig,scale,b):
    f=fig.resize((int(fig.width*scale),int(fig.height*scale)),Image.LANCZOS).crop((0,0,int(fig.width*scale),H-TOP))
    sh=Image.new('RGBA',f.size,(0,0,0,0)); sh.putalpha(f.split()[3].point(lambda a:int(a*.28)))
    sh=sh.filter(ImageFilter.GaussianBlur(28)); im=b.copy()
    im.paste(sh,(CX-f.width//2+18,TOP+22),sh); im.paste(f,(CX-f.width//2,TOP),f); return im
hero=Image.open(R+'/assets/site/img/hero.webp').convert('RGBA')
wave=Image.open(R+'/assets/site/img/wave.webp').convert('RGBA')
for k,(b0,g,e) in PAL.items():
    b=bg(b0,g,e)
    place(hero,970/1770,b).save(f'{S}/bg/{k}-start.png')
    place(wave,970/1319*.95,b).save(f'{S}/bg/{k}-end.png')
    place(hero,970/1770,b).resize((1600,900),Image.LANCZOS).save(f'{S}/bg/{k}-poster.webp',quality=88)
print('ok')
