import PyPDF2

pdffile1=r'C:/Users/ASUS/Downloads/7225.pdf'
pdffile2=r'C:/Users/ASUS/Downloads/7227.pdf'
pdffile3=r'C:/Users/ASUS/Downloads/7229.pdf'

merger=PyPDF2.PdfMerger()
for filename in pdffile1,pdffile2,pdffile3:
    pdffile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdffile)
    merger.append(pdfReader)
pdffile.close()
merger.write('merged.pdf')
