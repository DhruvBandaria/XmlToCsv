import xml.dom.minidom


def main(filename):
    doc = xml.dom.minidom.parse(filename)
    # print(doc.nodeName)
    customers = doc.getElementsByTagName("Customer")
    customerList =[]
    for customer in customers:
        customerList.append(customer.getAttribute("CustomerID"))

    print(customerList)
    orders = doc.getElementsByTagName("Order")
    orderDateList = []
    requiredDateList = []
    shippingDateList = []

    for order in orders:
        print(order.getElementsByTagName("OrderDate")[0].firstChild.nodeValue)
        print(order.getElementsByTagName("RequiredDate")[0].firstChild.nodeValue)
        print(order.getElementsByTagName("ShipInfo")[0].getAttribute("ShippedDate"))
        print("*"*40)




main("CustomerOrders.xml")
