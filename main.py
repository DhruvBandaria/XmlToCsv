import xml.dom.minidom
import csv

def main(filename):
    doc = xml.dom.minidom.parse(filename)
    # print(doc.nodeName)
    customers = doc.getElementsByTagName("Customer")
    customerList =[]
    for customer in customers:
        customerList.append(customer.getAttribute("CustomerID"))

    print(customerList)
    orders = doc.getElementsByTagName("Order")
    # orderDateList = []
    # requiredDateList = []
    # shippingDateList = []
    csvFields = ["Order Date", "Required Date", "Shipping Date"]

    for customer in customerList:
        file = open(customer+".csv", 'w')
        writer = csv.writer(file)
        writer.writerow(csvFields)
        for order in orders:
            if customer == order.getElementsByTagName("CustomerID")[0].firstChild.nodeValue:
                currentRow = [order.getElementsByTagName("OrderDate")[0].firstChild.nodeValue,
                              order.getElementsByTagName("RequiredDate")[0].firstChild.nodeValue,
                              order.getElementsByTagName("ShipInfo")[0].getAttribute("ShippedDate")]
                writer.writerow(currentRow)
        file.close()

    """
    for order in orders:
        orderDateList.append(order.getElementsByTagName("OrderDate")[0].firstChild.nodeValue)
        requiredDateList.append(order.getElementsByTagName("RequiredDate")[0].firstChild.nodeValue)
        shippingDateList.append(order.getElementsByTagName("ShipInfo")[0].getAttribute("ShippedDate")) 
    """

main("CustomerOrders.xml")
