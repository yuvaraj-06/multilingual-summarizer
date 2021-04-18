import pdfplumber

if pdf=='on':

    te=''
    pdf = pdfplumber.open(p)
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        te += page.extract_text()
    out = GoogleTranslator(source='en', target=lan).translate(text=te)
    t=gTTS(str(out),lang=lan)
    pdf.close()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    t.save("%s.mp3" % os.path.join(BASE_DIR+'/media',a))
    params={'out':out,'filePathName':filePathName+".mp3"}
    print(params)
    return render(request,'out.html',params)