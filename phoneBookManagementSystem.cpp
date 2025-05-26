#include<iostream>
#include<fstream>
using namespace std;
class Contact{
public:
int ch;
string name;
char number[15];
}c;
string s;
void add(){
cout<<"Enter the name : ";
cin>>c.name;
cout<<"Enter the number : ";
cin>>c.number;
ofstream output;
output.open("contacts.txt",ios::app);
output <<c.name << endl;
output<<c.number<<endl;
output.close();
}
void show_all_data(){
cout<<"All data of file is...\n";
ifstream input;
input.open("contacts.txt");
input>>c.name;
input>>c.number;
while(!input.eof()){
cout<<endl;
cout<<"Name :"<<c.name<<endl;
cout<<"Number :"<<c.number<<endl;
input>>c.name;
input>>c.number;
}
input.close();
}
void search(){
int count=0;
cout<<"Enter the name whose number you want :";
cin>>s;
ifstream input;
input.open("contacts.txt");
input>>c.name;
input>>c.number;
while(!input.eof()){
input>>c.name;
input>>c.number;
if(c.name==s)
{
cout<<"\nName : "<<c.name;
cout<<"\nNumber : "<<c.number;
count++;
break;
}
}
if(count==0){
cout<<"\nrecord not found\n";
}
input.close();
}
void delete_a_contact(){
cout<<"Witch contact do you want to delete : ";
cin>>s;
ifstream input;
input.open("contacts.txt");
ofstream output;
output.open("new.txt");
input>>c.name;
input>>c.number;
while(!input.eof()){
if(c.name!=s)
{
output<<c.name<<endl;
output<<c.number<<endl;
}
else{
cout<<"Contanct is deleted";
}
input>>c.name;
input>>c.number;
}
output.close();
input.close();
remove("contacts.txt");
rename("new.txt","contacts.txt");
}
void delete_all(){
ofstream output;
output.open("contacts.txt",ios::out | ios::trunc);
output.close();
cout<<"All data is deleted...";
}
int main(){
while (1){
cout<<"\n------------------Contact list-----------------------\n";
cout<<"Enter New contact press[1]\n";
cout<<"Display all contact press[2]\n";
cout<<"Find a contact press[3]\n";
cout<<"Remove a contact press[4]\n";
cout<<"Remove all contacts press[5]\n";
cout<<"Close the file press[6]\n";
cout<<"----------------------------------------------------\n";
cin>>c.ch;
if (c.ch==6){break;}
switch (c.ch){
case 1:
add();
break;
case 2:
show_all_data();
break;
case 3:
search();
break;
case 4:
delete_a_contact();
break;
case 5:
delete_all();
break;
}
}
}
