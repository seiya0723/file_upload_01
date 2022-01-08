from django.shortcuts import render, redirect
from django.views import View
from .models import Document
from .forms import DocumentForm
import magic
AllOWED_MIME = ["image/jpeg", "application/zip", "video/mp4", "application/pdf"]

class IndexView(View):

    def get(self, request, *args, **kwargs):
        documents = Document.objects.all()
        context = {"documents":documents}


        return render(request,"dojo/index.html", context)


    def post(self, request, *args, **kwargs):

        #アップロードファイルが存在しない場合、リダイレクト
        if "content" not in request.FILES:
            return redirect("dojo:index")

        #mimeの取得、mimeをセットしたリクエストをバリデーションする。
        mime    = magic.from_buffer(request.FILES["content"].read(1024), mime=True)

        #TIPS:クライアントから受け取ったリクエストを直接書き換えすることはできない。そのためcopyメソッドでリクエストのコピーを作る。
        copied          = request.POST.copy()
        copied["mime"]  = mime
        
        form = DocumentForm(copied, request.FILES)

        if form.is_valid():
            print("バリデーションOK")
            # 保存する

            if mime in AllOWED_MIME:
                form.save()
            else:
                print("このファイルは許可されていません")


        else:
            print("バリデーションNG")
            print(mime)


        return redirect("dojo:index")


index   = IndexView.as_view()
