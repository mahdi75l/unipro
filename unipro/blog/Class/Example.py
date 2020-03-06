import operator

from ..models import Category, Post


def getListPost(id):
    listPost = []
    current_category = Category.objects.filter(parent=id)
    print("child category :")
    print(current_category)
    for categoryID in current_category:
        nextList = getListPost(categoryID.id)
        print(nextList)
        for item in nextList:
            listPost.append(item)
    for item in Post.objects.filter(category=id):
        listPost.append(item)
    print("this is final list:")
    print(listPost)
    return listPost


def getPostCategory(id):
    List = getListPost(id)
    ordered = sorted(List, key=operator.attrgetter('created'))
    return ordered

