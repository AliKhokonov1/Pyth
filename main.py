import sys
from PIL import Image
def main(N1,N2,N,infile,outfile):
    try:
        #Загружаем изображение с жесткого диска
        myim = Image.open(infile)
    except FileNotFoundError:
        print("Файл не найден")
        return
    if myim.mode != 'RGB' and myim.mode != 'RGBA':
        print("Неверный формат файла")
        return
    F=0;
    if N1 > N2 :
        F=N1
        N1=N2
        N2=F
    for x in range(myim.shape[0]):
        for y in range(myim.shape[1]):
            R, G, B = myim[x, y]
            if N1 <= sum([R,G,B]) <= N2:
                myim[x,y]=(N,N,N)
    myim.save(outfile,"bmp")

if __name__ == "__main__":
     print("Input Image name")
     inim = input()

     print("Output Image name")
     outim = input()

     print("First brightness")
     K1 = int(input())

     print("Second brightness")
     K2 = int(input())

     print("Your components")
     K = int(input())

     main(K1,K2,K,inim,outim)
