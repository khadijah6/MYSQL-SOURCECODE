#Server

from http.server import HTTPServer, BaseHTTPRequestHandler
from restaurantDatabase import RestaurantDatabase
import cgi

class RestaurantPortalHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.database = RestaurantDatabase()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == '/addReservation':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )

            try:
                customer_id = int(form.getvalue("customer_id"))
                reservation_time = form.getvalue("reservation_time")
                number_of_guests = int(form.getvalue("number_of_guests"))
                special_requests = form.getvalue("special_requests")

                # Call the Database Method to add a new reservation
                self.database.addReservation(customer_id, reservation_time, number_of_guests, special_requests)
                print("Reservation added for customer ID:", customer_id)

                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                                 <a href='/addReservation'>Add Reservation</a> | \
                                 <a href='/viewReservations'>View Reservations</a> | \
                                 <a href='/deleteReservation'>Delete Reservation</a> | \
                                 <a href='/addCustomer'>Add Customer</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservation has been added successfully</h3>")
                self.wfile.write(b"<div><a href='/addReservation'>Add Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")
            except (TypeError, ValueError) as e:
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                                 <a href='/addReservation'>Add Reservation</a> | \
                                 <a href='/viewReservations'>View Reservations</a> | \
                                 <a href='/deleteReservation'>Delete Reservation</a> | \
                                 <a href='/addCustomer'>Add Customer</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Error: Please provide valid inputs.</h3>")
                self.wfile.write(b"<div><a href='/addReservation'>Try Again</a></div>")
                self.wfile.write(b"</center></body></html>")

        elif self.path == '/deleteReservation':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )

            try:
                reservation_id = int(form.getvalue("reservation_id"))

                # Call the Database Method to delete a reservation by ID
                self.database.deleteReservation(reservation_id)
                print("Reservation deleted with ID:", reservation_id)

                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                                 <a href='/addReservation'>Add Reservation</a> | \
                                 <a href='/viewReservations'>View Reservations</a> | \
                                 <a href='/deleteReservation'>Delete Reservation</a> | \
                                 <a href='/addCustomer'>Add Customer</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservation has been deleted successfully</h3>")
                self.wfile.write(b"<div><a href='/deleteReservation'>Delete Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")
            except (TypeError, ValueError) as e:
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                                 <a href='/addReservation'>Add Reservation</a> | \
                                 <a href='/viewReservations'>View Reservations</a> | \
                                 <a href='/deleteReservation'>Delete Reservation</a> | \
                                 <a href='/addCustomer'>Add Customer</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Error: Please provide valid inputs.</h3>")
                self.wfile.write(b"<div><a href='/deleteReservation'>Try Again</a></div>")
                self.wfile.write(b"</center></body></html>")
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
            self.wfile.write(b"<body>")
            self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addReservation'>Add Reservation</a> | \
                             <a href='/viewReservations'>View Reservations</a> | \
                             <a href='/deleteReservation'>Delete Reservation</a> | \
                             <a href='/addCustomer'>Add Customer</a></div>")
            self.wfile.write(b"<hr><h2>All Reservations</h2>")
            records = self.database.getAllReservations()
            if records:
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Reservation ID </th>\
                                        <th> Customer ID </th>\
                                        <th> Reservation Time </th>\
                                        <th> Number of Guests </th>\
                                        <th> Special Requests </th></tr>")
                for row in records:
                    self.wfile.write(b'<tr><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                self.wfile.write(b"</table>")
            else:
                self.wfile.write(b"<p>No reservations found</p>")
            self.wfile.write(b"</center>")
            self.wfile.write(b"</body></html>")
        elif self.path == '/addReservation':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><head><title>Add Reservation</title></head>")
            self.wfile.write(b"<body><center><h1>Add Reservation</h1>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addReservation'>Add Reservation</a> | \
                             <a href='/viewReservations'>View Reservations</a> | \
                             <a href='/deleteReservation'>Delete Reservation</a> | \
                             <a href='/addCustomer'>Add Customer</a></div>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<form method='POST' action='/addReservation'>")
            self.wfile.write(b"Customer ID: <input type='text' name='customer_id'><br>")
            self.wfile.write(b"Reservation Time: <input type='text' name='reservation_time'><br>")
            self.wfile.write(b"Number of Guests: <input type='text' name='number_of_guests'><br>")
            self.wfile.write(b"Special Requests: <input type='text' name='special_requests'><br>")
            self.wfile.write(b"<input type='submit' value='Add Reservation'>")
            self.wfile.write(b"</form></center></body></html>")
        elif self.path == '/viewReservations':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            records = self.database.getAllReservations()
            self.wfile.write(b"<html><head><title>View Reservations</title></head>")
            self.wfile.write(b"<body><center><h1>View Reservations</h1>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addReservation'>Add Reservation</a> | \
                             <a href='/viewReservations'>View Reservations</a> | \
                             <a href='/deleteReservation'>Delete Reservation</a> | \
                             <a href='/addCustomer'>Add Customer</a></div>")
            self.wfile.write(b"<hr>")
            if records:
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Reservation ID </th>\
                                        <th> Customer ID </th>\
                                        <th> Reservation Time </th>\
                                        <th> Number of Guests </th>\
                                        <th> Special Requests </th></tr>")
                for row in records:
                    self.wfile.write(b'<tr><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                self.wfile.write(b"</table>")
            else:
                self.wfile.write(b"<p>No reservations found</p>")
            self.wfile.write(b"</center>")
            self.wfile.write(b"</body></html>")
        elif self.path == '/deleteReservation':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><head><title>Delete Reservation</title></head>")
            self.wfile.write(b"<body><center><h1>Delete Reservation</h1>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addReservation'>Add Reservation</a> | \
                             <a href='/viewReservations'>View Reservations</a> | \
                             <a href='/deleteReservation'>Delete Reservation</a> | \
                             <a href='/addCustomer'>Add Customer</a></div>")
            self.wfile.write(b"<hr>")
            self.wfile.write(b"<form method='POST' action='/deleteReservation'>")
            self.wfile.write(b"Reservation ID: <input type='text' name='reservation_id'><br>")
            self.wfile.write(b"<input type='submit' value='Delete Reservation'>")
            self.wfile.write(b"</form></center></body></html>")
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

def run(server_class=HTTPServer, handler_class=RestaurantPortalHandler, port=8002):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
