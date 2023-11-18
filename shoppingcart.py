class basket:
    def details(product):
        product.name=["lw","umbrella","cigarette","honey"]
        product.price=[1100,900,200,100]
        product.gst=[18,12,28,0]
        product.quantity=[1,4,3,2]
    def maxgst(product):
        for i in range(0,4):
            if product.gst[i]>0:
                g=product.price[i]*(product.gst[i])/100
        mgst=[]
        mgst.append(g)
        maxg=max(mgst)
        j=mgst.index(maxg)
        name=product.name(j)
        print('the product with maximum GST amount is{}'.format(name))
        
    def totalamount(product):
        for i in range(0,4):
            if product.price[i]>=500:
                product.price[i]=product.price[i]-(product.price[i]*(5/100))
        for i in range(0,4):
            a=(product.price[i]+mgst[i])* product.quantity[i]
        tamount=[]
        tamount.append(a)
        total_price=0
        for i in range(0,4):
            total_price=total_price+tamount[i]
        print('the total amount paid to the shop keeper is {}'.format(total_price))

product=basket()
product.details()
product.maxgst()
product.totalamount()
