"""
Authors: [Your Name]
Simulation1: Implements the simulation with a separate queue for each cash register.
"""

import random
from collections import deque
from customer import Customer

def simulate_separate_queues(arrival_probability, num_registers, total_minutes):
    # Create a separate queue for each register.
    queues = [deque() for _ in range(num_registers)]
    # Each register either holds a tuple (customer, remaining_service_time) or None if free.
    registers = [None for _ in range(num_registers)]
    
    waiting_times = []

    for current_minute in range(total_minutes):
            # INSERT CODE HERE
            #  Use the customerArrives method to determine if a customer
            #  arrives at this particular minute.
            #  If so, add a customer to the queue.



            # INSERT CODE HERE
            # Check each register.
            #   If the register is available and there are customers waiting in the queue,
            #     1.  Remove the customer at the front of the queue.
            #     2.  Update the total number of customers who have successfully 
            #         reached a register
            #     3.  Update the total time that each customer has spent waiting 
            #         in the queue before successfully reaching a register
            #     4.  Update the time when this register will be available after
            #         serving this customer.
        customer = customer_arrives(arrival_probability, current_minute)
        if customer is not None:
            shortest_queue = queues[0]
            for i in queues:
                if len(i) < len(shortest_queue):
                    shortest_queue = i
            shortest_queue.append(customer)

        for i in range(num_registers):
            if registers[i]:
                customer, remaining_service_time = registers[i]
                remaining_service_time -= 1
                if remaining_service_time <= 0:
                    waiting_times.append(current_minute - customer.arrival_time)
                    registers[i] = None
                else:
                    registers[i] = (customer, remaining_service_time)

            if registers[i] is None:
                if queues[i]:
                    customer = queues[i].popleft()
                    # print(customer)
                    registers[i] = (customer, customer.service_time)
    average_wait = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    return average_wait


def customer_arrives(arrival_probability, current_minute):
    if random.random() < arrival_probability:
        service_time = random.randint(1, 3)
        return Customer(current_minute, service_time)
    return None

if __name__ == "__main__":
    # Simulation parameters
    arrival_probability = 0.3
    num_registers = 3
    total_minutes = 1000

    avg_wait = simulate_separate_queues(arrival_probability, num_registers, total_minutes)
    print(f"Average waiting time (separate queues): {avg_wait:.2f} minutes")
