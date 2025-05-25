#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SEATS 10
typedef struct {
int seatNum;
char name[50];
} Reservation;
Reservation reservationList[MAX_SEATS];
void initReservations() {
int i;
for(i = 0; i < MAX_SEATS; i++) {
reservationList[i].seatNum = i + 1;
strcpy(reservationList[i].name, "empty");
}
}
void displaySeats() {
int i;
printf("Seat # Passenger Name\n");
for(i = 0; i < MAX_SEATS; i++) {
printf("%d %s\n", reservationList[i].seatNum, reservationList[i].name);
}
}
void bookSeat() {
int seatNum;
char name[50];
printf("Enter seat number to book: ");
scanf("%d", &seatNum);
if(seatNum < 1 || seatNum > MAX_SEATS) {
printf("Invalid seat number.\n");
return;
}
if(strcmp(reservationList[seatNum-1].name, "empty") != 0) {
printf("Seat already booked.\n");
return;
}
printf("Enter passenger name: ");
scanf("%s", name);
strcpy(reservationList[seatNum-1].name, name);
printf("Booking successful.\n");
}
void cancelSeat() {
int seatNum;
printf("Enter seat number to cancel: ");
scanf("%d", &seatNum);
if(seatNum < 1 || seatNum > MAX_SEATS) {
printf("Invalid seat number.\n");
return;
}
if(strcmp(reservationList[seatNum-1].name, "empty") == 0) {
printf("Seat already empty.\n");
return;
}
strcpy(reservationList[seatNum-1].name, "empty");
printf("Cancellation successful.\n");
}
int main() {
printf(“\n\t\tWelcome to Airline Site\n”);
int choice;
initReservations();
while(1) {
printf("\n1. Display seats\n");
printf("2. Book seat\n");
printf("3. Cancel seat\n");
printf("4. Exit\n");
printf("Enter choice: ");
scanf("%d", &choice);
switch(choice) {
case 1:
displaySeats();
break;
case 2:
bookSeat();
break;
case 3:
cancelSeat();
break;
case 4:
exit(0);
default:
printf("Invalid choice.\n");
}
}
return 0;
}
