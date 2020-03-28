#Creating a system to calculate ticket sales

class TicketSales:

    def __init__(self, cell_num, price_of_ticket, no_of_tickets):
        self.cell_num = cell_num
        self.price_of_ticket = price_of_ticket
        self.no_of_tickets = no_of_tickets

#Creating the function to calculate payment

    def cal_Prepayment(self):
        amount = self.price_of_ticket * self.no_of_tickets
        _VAT = 0.15
        amount_due = amount + (amount * _VAT)
        return amount_due

#creating the function to give the correct amount to each category
def Ticket_Amount(category):
    if category == "Theatre":
     return 100
    elif category == "Soccer":
     return 75
    elif category == "Movie":
     return 40

#creating the variables for the selection by the customer
category = input("Please enter what you would like to watch (Theatre/Soccer/Movie): \n")
client = input("Please enter cell number: \n")
amount_ticket = int(input("Please enter how much tickets you would like: \n"))

ticket_type = Ticket_Amount(category)
ticket = TicketSales(client , ticket_type , amount_ticket)
total_due = ticket.cal_Prepayment()


#displaying the receipt
print("Customer cellphone number is", client)
print("Ticket price excluding VAT R", ticket_type)
print("This is the amount of Tickets your are purchasing:", amount_ticket)
print("This is the ticket price including VAT: R", total_due)






















