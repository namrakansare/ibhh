from django.shortcuts import render
# Create your views here.
posts=[
{
"author":"vraj Patel",
"title":"Blog Post 1 "
},
{
"author":"raj Jayswal",
"title":"Blog Post 1 "
}
]
def home(request):
	context = {
	 "posts":posts
	}
	return render(request,"blog/home.html",context)
def about(request):
	return render(request,"blog/about.html")