import java.io.*;
import java.util.*;
class User {
private String username;
private String password;
private double balance;
public User(String username, String password, double balance) {
this.username = username;
this.password = password;
this.balance = balance;
}
public String getUsername() {
return username;
}
public String getPassword() {
return password;
}
public double getBalance() {
return balance;
}
public void deposit(double amount) {
balance += amount;
System.out.println("Deposit successful. Current balance: " + balance);
}
public boolean withdraw(double amount) {
if (balance >= amount) {
balance -= amount;
System.out.println("Withdrawal successful. Current balance: " + balance);
return true;
} else {
System.out.println("Insufficient funds.");
return false;
}
}
}
public class BankingSystem {
private static final String USER_DATA_FILE = "userdata.txt";
private static final List<User> users = new ArrayList<>();
public static void main(String[] args) {
loadUserData();
Scanner scanner = new Scanner(System.in);
System.out.println("Welcome to the Banking System!");
while (true) {
System.out.println("\n1. Login\n2. Create New Account\n3. Exit");
System.out.print("Enter your choice: ");
int choice = scanner.nextInt();
scanner.nextLine(); // Consume newline
switch (choice) {
case 1:
login(scanner);
break;
case 2:
createAccount(scanner);
break;
case 3:
System.out.println("Exiting...");
System.exit(0);
default:
System.out.println("Invalid choice. Please try again.");
}
}
}
private static void loadUserData() {
try (Scanner fileScanner = new Scanner(new File(USER_DATA_FILE))) {
while (fileScanner.hasNextLine()) {
String line = fileScanner.nextLine();
String[] parts = line.split(",");
if (parts.length == 3) {
users.add(new User(parts[0], parts[1], Double.parseDouble(parts[2])));
}
}
} catch (FileNotFoundException e) {
// File doesn't exist yet, so we'll create it when saving user data
}
}
private static void saveUserData() {
try (PrintWriter writer = new PrintWriter(new FileWriter(USER_DATA_FILE))) {
for (User user : users) {
writer.println(user.getUsername() + "," + user.getPassword() + "," + user.getBalance());
}
} catch (IOException e) {
e.printStackTrace();
}
}
private static void login(Scanner scanner) {
System.out.print("Enter username: ");
String username = scanner.nextLine();
System.out.print("Enter password: ");
String password = scanner.nextLine();
for (User user : users) {
if (user.getUsername().equals(username) && user.getPassword().equals(password)) {
System.out.println("Login successful!");
while (true) {
System.out.println("\n1. Deposit\n2. Withdraw\n3. Logout");
System.out.print("Enter your choice: ");
int choice = scanner.nextInt();
scanner.nextLine(); // Consume newline
switch (choice) {
case 1:
System.out.print("Enter amount to deposit: ");
double depositAmount = scanner.nextDouble();
user.deposit(depositAmount);
saveUserData();
break;
case 2:
System.out.print("Enter amount to withdraw: ");
double withdrawAmount = scanner.nextDouble();
user.withdraw(withdrawAmount);
saveUserData();
break;
case 3:
System.out.println("Logging out...");
return;
default:
System.out.println("Invalid choice. Please try again.");
}
}
}
}
System.out.println("Username or password incorrect. Please try again.");
}
private static void createAccount(Scanner scanner) {
System.out.print("Enter new username: ");
String newUsername = scanner.nextLine();
System.out.print("Enter new password: ");
String newPassword = scanner.nextLine();
System.out.print("Enter initial balance: ");
double initialBalance = scanner.nextDouble();
users.add(new User(newUsername, newPassword, initialBalance));
saveUserData();
System.out.println("Account created successfully!");
}
}
