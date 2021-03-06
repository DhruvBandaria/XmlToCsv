import xml.dom.minidom
import csv
from datetime import datetime


def main(filename):
    doc = xml.dom.minidom.parse(filename)
    customers = doc.getElementsByTagName("Customer")
    customerList = []
    for customer in customers:
        customerList.append(customer.getAttribute("CustomerID"))

    orders = doc.getElementsByTagName("Order")
    csvFields = ["Order Date", "Required Date", "Shipping Date"]

    for customer in customerList:
        file = open(customer + ".csv", 'w')
        writer = csv.writer(file)
        writer.writerow(csvFields)
        for order in orders:
            if customer == order.getElementsByTagName("CustomerID")[0].firstChild.nodeValue:
                currentRow = []
                if order.getElementsByTagName("OrderDate")[0].firstChild.nodeValue != '':
                    currentRow.append(datetime.strptime(order.getElementsByTagName("OrderDate")[0].firstChild.nodeValue,
                                                        '%Y-%m-%dT%H:%M:%S'))
                else:
                    currentRow.append('NIL')
                if order.getElementsByTagName("RequiredDate")[0].firstChild.nodeValue != '':
                    currentRow.append(
                        datetime.strptime(order.getElementsByTagName("RequiredDate")[0].firstChild.nodeValue,
                                          '%Y-%m-%dT%H:%M:%S'))
                else:
                    currentRow.append('NIL')
                if order.getElementsByTagName("ShipInfo")[0].getAttribute("ShippedDate") != '':
                    currentRow.append(
                        datetime.strptime(order.getElementsByTagName("ShipInfo")[0].getAttribute("ShippedDate"),
                                          '%Y-%m-%dT%H:%M:%S'))
                else:
                    currentRow.append('NIL')
                writer.writerow(currentRow)
        file.close()


main("CustomerOrders.xml")
