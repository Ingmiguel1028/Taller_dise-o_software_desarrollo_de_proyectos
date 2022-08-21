import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, cliente, asunto):
        self.id = generate_id()
        self.cliente = cliente
        self.asunto = asunto


class estrategia_orden_ticket(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class estrategia_fifo(estrategia_orden_ticket):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class estrategia_filo(estrategia_orden_ticket):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class estrategia_Random(estrategia_orden_ticket):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class estrategia_Blackhole(estrategia_orden_ticket):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []


class clienteSupport:

    def __init__(self, processing_strategy: estrategia_orden_ticket):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, cliente, asunto):
        self.tickets.append(SupportTicket(cliente, asunto))

    def process_tickets(self):
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"cliente: {ticket.cliente}")
        print(f"asunto: {ticket.asunto}")
        print("==================================")


# create the application
app = clienteSupport(estrategia_Random())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
