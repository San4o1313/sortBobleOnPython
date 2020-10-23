import pygame
import time
from random import choice
pygame.mixer.init()
pygame.mixer.music.load("\windows\media\chimes.wav")

sm = 30
sise = int((470-sm)/(sm+2))
spd = 0.05
Hi = We = sise* sm+ 2*sise+ sm
BLACK = (0,0,0)
GREY = (220,220,220)
sc = pygame.display.set_mode((We,Hi))

def rnd_lst(ln):
	x = list(range(1,ln+1))
	for i in range(ln):
		b=choice(x[:ln+1-i])
		x.append(b)
		x.remove(b)	
	return x

def diagr(a,sise,itr = -1):
	x=0
	for i in range(len(a)):
				x+=sise+1
				y=Hi-sise
				for j in range(a[i]):
					y-=sise+1
					if i == itr+1:
						pygame.draw.rect(sc,(250,0,0),(x,y,sise,sise))
					else:
						pygame.draw.rect(sc,(BLACK),(x,y,sise,sise))

# main loop 
def main():
	while 1:
		a = rnd_lst(sm)
		psg = 1
		for i in range(len(a)-1):
			sc.fill(GREY)
			diagr(a,sise)
			pygame.display.flip()
			time.sleep(spd)
			for itr in range(len(a)-psg):	
				for i in pygame.event.get():  
					if i.type == pygame.QUIT:
						pygame.quit()
						exit() 		
				if a[itr]>a[itr+1]:
					a[itr],a[itr+1]=a[itr+1],a[itr] 
				sc.fill(GREY)
				diagr(a,sise,itr)
				pygame.display.flip()
				time.sleep(spd)
			pygame.mixer.music.play(0)	
			if a == sorted(a):
				break
			psg+=1



		for k in range(2,9):	
			x=0		
			for i in range(len(a)):
				x+=sise+1
				y=Hi-sise
				for j in range(a[i]):
					y-=sise+1
					if k%2 == 1:
						pygame.draw.rect(sc,(250,0,0),(x,y,sise,sise))
					else:
						pygame.draw.rect(sc,(BLACK),(x,y,sise,sise))
				time.sleep(0.01)	
				pygame.display.flip()	

if __name__ == '__main__':
    main()