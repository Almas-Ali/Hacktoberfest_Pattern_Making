/*
 *Author: Pasindu Akalpa
 */

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class VaccinationCenter {
    private static String[] vaccinationBooth = new String[6]; // Create size 6 empty String array object
    private static int vaccineCount = 150; // Center vaccine Count
    private static final Scanner scanner = new Scanner(System.in); // Create scanner object from Scanner Class
    private static boolean[] isEditable = new boolean[6]; // Create array to is booth occupied or not
    private static boolean isValid = true; // loop control variable of mainMenu method

    /**
     * Main Method Invoke two methods
     *
     * @param args None
     */
    public static void main(String[] args) {
        asciiArt();
        initialise(); // Invoke initialise method
        mainMenu(); // Invoke MainMenuRender Method
    }

    /**
     * Initialise String array as empty beginning of the program
     */
    private static void initialise() {
        for (int i = 0; i < 6; i++) {
            vaccinationBooth[i] = "*"; // add "*" as array elements
            isEditable[i] = true; // add true as array elements
        }
    }

    /**
     * This Method Display COVID-19 V.C Program  Console Main Menu
     */
    public static void mainMenu() {
        while (isValid) {
            warningMsg(); // Invoke Warning Message Method
            String menuItems = "\n------------------------------------------------------------"
                    .concat("\n|           COVID-19 VACCINATION CENTER Program            |")
                    .concat("\n|----------------------------------------------------------|")
                    .concat("\n| 100 or VVB |\tView all Vaccination Booths                |")
                    .concat("\n| 101 or VEB |\tView all Empty Booths                      |")
                    .concat("\n| 102 or APB |\tAdd Patient to a Booth                     |")
                    .concat("\n| 103 or RPB |\tRemove Patient from a Booth                |")
                    .concat("\n| 104 or VPS |\tView Patients Sorted in alphabetical order |")
                    .concat("\n| 105 or SPD |\tStore Program Data into file               |")
                    .concat("\n| 106 or LPD |\tLoad Program Data from file                |")
                    .concat("\n| 107 or VRV |\tView Remaining Vaccinations                |")
                    .concat("\n| 108 or AVS |\tAdd Vaccinations to the Stock              |")
                    .concat("\n| 999 or EXT |\tExit the Program                           |")
                    .concat("\n------------------------------------------------------------")
                    .concat("\nChoose Option: "); // Console Main Menu String
            System.out.print(menuItems);
            boolean hasNext = scanner.hasNext();
            if (hasNext) {
                String code = scanner.next().toUpperCase(); // get user input and store in code variable
                mainMenuInputValidation(code); // Invoke menuInputValidation method and parse code as argument
            }
        }
        System.out.println("Exiting Program...");
    }

    /**
     * This Method Validates Main Menu Inputs
     *
     * @param code User Input String
     */
    private static void mainMenuInputValidation(String code) {
        boolean validInput = false;
        String[] validInputArray = {"100", "VVB", "101", "VEB", "102", "APB", "103", "RPB", "104", "VPS", "105",
                "SPD", "106", "LPD", "107", "VRV", "108", "AVS", "999", "EXT"}; // valid Inputs hard coded into string array
        int index = 0;

        for (int i = 0; i < validInputArray.length; i++) {
            if (code.equals(validInputArray[i])) {
                validInput = true;
                index = i;
            }
        }

        if (validInput) {
            switch (index) { // switch case of valid input index
                // 100 or VVB
                case 0, 1 -> viewAllBooths();
                //101 or VEB
                case 2, 3 -> viewAllEmptyBooths();
                //102 or APB
                case 4, 5 -> addPatient();
                //103 or RPB
                case 6, 7 -> removePatient();
                //104 or VPS
                case 8, 9 -> sortPatientNames();
                //105 or SPD
                case 10, 11 -> saveProgramData();
                //106 or LPD
                case 12, 13 -> loadProgramData();
                //107 or VRV
                case 14, 15 -> viewRemainingVaccines();
                //108 or AVS
                case 16, 17 -> addVaccinesToStock();
                case 18, 19 -> isValid = false;
            }
        } else {
            isValid = true;
            System.out.println("Invalid Input! Try Again.");
        }
    }

    /**
     * This Method Contains all the logics for Menu item 1 (100 or VVB: View all Vaccination Booths)
     */
    private static void viewAllBooths() {
        System.out.println("\nList of All Vaccination Booths");
        for (int i = 0; i < 6; i++) {
            if (vaccinationBooth[i].equals("*")) {
                System.out.println("Booth " + i + " is Empty"); // Show Empty Booths Only
            } else {
                System.out.println("Booth " + i + " is occupied by " + vaccinationBooth[i]); // Show occupied booth with patient name
            }
        }
    }

    /**
     * This Method Contains all the logics for Menu item 2 (101 or VEB: View all Empty Booths)
     */
    private static void viewAllEmptyBooths() {
        System.out.println("\nList of Empty Vaccination Booths");
        int emptyBoothCount = 0; // Variable to store empty booth count
        for (int i = 0; i < vaccinationBooth.length; i++) {
            if (vaccinationBooth[i].equals("*")) { // Check for empty booths
                System.out.println("Booth " + i + " is Empty");
                emptyBoothCount++; //increment empty booth count by one
            }
        }
        if (emptyBoothCount == 0) { // check for empty booth count is equal to zero
            System.out.println("All Booths Are Occupied!");
        }
    }

    /**
     * This Method List All the Occupied Vaccination Booths
     */
    private static void viewAllOccupiedBooths() {
        System.out.println("\nList of Occupied Vaccination Booths");
        for (int i = 0; i < vaccinationBooth.length; i++) {
            if (!vaccinationBooth[i].equals("*")) {
                System.out.println("Booth " + i + " is occupied by " + vaccinationBooth[i]);
            }
        }
        System.out.println(" ");
    }

    /**
     * This Method Add Patient to Array
     */
    private static void addPatient() {
        while (true) {
            int boothNumber;
            String patientName;
            char returnChar = boothChecker(); // invoke boothChecker Method and store return value
            if (returnChar == 'N') {
                System.out.println("All booths Are Occupied!\nTry Removing Assigned Patient using Option in Main Menu -> Remove Patient from a Booth");
                break;
            }
            viewAllEmptyBooths(); // invoke viewAllEmptyBooths method
            do { // this loop validates user input
                System.out.print("Enter Booth Number (0 - 5) to Add Patient or 6 to go back to Main Menu: ");
                while (!scanner.hasNextInt()) {
                    System.out.print("Invalid Input! Try Again.\nEnter Booth Number (0 - 5) or 6 to go back to Main Menu: ");
                    scanner.next();
                }
                boothNumber = scanner.nextInt();
                if (boothNumber > 6 || boothNumber < 0) {
                    System.out.println("Invalid Input! Try Again.");
                }
            } while ((boothNumber < 0) || (boothNumber > 6));
            if (boothNumber == 6) {
                System.out.println("Back to Main Menu....");
                break;
            } else if (vaccineCount == 0) {
                System.out.println("No! Vaccines Remaining. Restock Required!\n\n");
                break;
            } else if (isEditable[boothNumber]) {
                System.out.print("Enter Patient Name for Booth " + boothNumber + " : ");
                patientName = scanner.next();
                vaccinationBooth[boothNumber] = patientName; // assign name to array
                vaccineCount--; // decrease vaccine count
                isEditable[boothNumber] = false; // assign false to make selected booth occupied
                System.out.println("Update Successful!\n");
            } else {
                System.out.println("Patient already Assigned to Booth No: " + boothNumber + ". wait until Assigned Patient get Vaccinated.\nOr Try Removing Assigned Patient using Option in Main Menu -> Remove Patient from a Booth\n");
            }
        }
    }

    /**
     * This Method Remove Patient from Array
     */
    private static void removePatient() {
        while (true) {
            int boothNumber;
            char returnChar = boothChecker(); // invoke boothChecker method and store return value
            if (returnChar == 'Y') {
                System.out.println("All booths Are Empty\nTry Adding Patient using Option in Main Menu -> Add Patient to a Booth");
                break;
            }
            viewAllOccupiedBooths(); // invoke viewAllOccupiedBooths method
            do { // this loop validates user input
                System.out.print("Enter Booth Number (0 - 5) to Remove Patient or 6 to go back to Main Menu: ");
                while (!scanner.hasNextInt()) {
                    System.out.print("Invalid Input! Try Again.\nEnter Booth Number (0 - 5) to Remove Patient or 6 to go back to Main Menu: ");
                    scanner.next();
                }
                boothNumber = scanner.nextInt();
                if (boothNumber > 6 || boothNumber < 0) {
                    System.out.println("Invalid Input! Try Again.");
                }
            } while ((boothNumber < 0) || (boothNumber > 6));
            if (boothNumber <= 5) {
                if (!vaccinationBooth[boothNumber].equals("*")) {
                    vaccinationBooth[boothNumber] = "*";
                    isEditable[boothNumber] = true;
                    System.out.println("Remove Successful!");
                } else {
                    System.out.println("Selected Booth is Already Empty");
                }
            } else {
                System.out.println("Back to Main Menu....");
                break;
            }
        }
    }

    /**
     * This Method Sort Patient Names in Alphabetical Order
     */
    private static void sortPatientNames() {
        System.out.println("\nPatient Names Sorted in Alphabetical Order");
        String temporaryString;
        int occupiedBoothCount = 0;
        int arrayLength = vaccinationBooth.length; // store length of vaccinationBooth(String[]) array
        String[] patientNameArray = new String[arrayLength];
        for (int i = 0; i < arrayLength; i++) {
            patientNameArray[i] = vaccinationBooth[i].substring(0,1).toUpperCase() + vaccinationBooth[i].substring(1);
        }
        String[] newArray = Arrays.copyOf(patientNameArray, arrayLength);
        /*
        * ritikasharma23
        * 24/06/2021
        * Java Program to Sort Names in an Alphabetical Order
        * https://www.geeksforgeeks.org/java-program-to-sort-names-in-an-alphabetical-order/
        * */
        for (int i = 0; i < newArray.length; i++) {
            for (int j = i + 1; j < newArray.length; j++) {
                if (newArray[i].compareTo(newArray[j]) > 0) {
                    temporaryString = newArray[i];
                    newArray[i] = newArray[j];
                    newArray[j] = temporaryString;
                }
            }
        }
        for (String s : newArray) {
            int index = Arrays.asList(patientNameArray).indexOf(s);
            if (!s.equals("*")) { // check for occupied booths
                System.out.println(s + " (Booth NO " + index + ")");
                occupiedBoothCount++;
            }
        }
        if (occupiedBoothCount == 0) {
            System.out.println("All Booths are Empty!. No name to Sort \n\t\t\t¯\\_(ツ)_/¯");
        }
    }

    /**
     * This Method Saves Program Data to file
     * Saving (Vaccine Count , Vaccination Booth Array, isEditable Array)
     */
    private static void saveProgramData() {
        if (!(boothChecker() == 'Y')) {
            try {
                System.out.println("File Saving....");
                File file = new File("./saveData/"); // create new File object

                if (!file.exists()) {
                    Files.createDirectory(Path.of("./saveData/"));
                }

                String saveFilename = new SimpleDateFormat("yyyyMMdd_HHmmss'.dat'").format(new java.util.Date()); // use date and time as unique name for save files
                String saveFilePath = "./saveData/" + saveFilename; // file name concatenated with file path

                FileOutputStream saveDataFile = new FileOutputStream(saveFilePath); // create new FileOutputStream object and parse saveFilePath string as argument
                ObjectOutputStream saveFile = new ObjectOutputStream(saveDataFile); // create new ObjectOutputStream object and parse saveDataFile object as argument

                saveFile.writeInt(vaccineCount); // write vaccine count to file
                saveFile.writeObject(vaccinationBooth); // write vaccinationBooth(String[]) array to file
                saveFile.writeObject(isEditable); // write isEditable(boolean[]) array to file

                System.out.println("File Saved Successfully!");
            } catch (Exception e) {
                System.out.println("Oops! Something went Wrong.");
            }
        } else {
            System.out.println("All Booths Are Empty\nNothing to Save.");
        }
    }

    /**
     * This Method load Save file (.dat) to program
     */
    private static void loadProgramData() {
        try {
            int saveDataIndex;
            String[] saveFileList; // define empty string array for store saved file names
            File file = new File("./saveData/"); // Create new File object

            FilenameFilter filenameFilter = (dir, name) -> name.endsWith(".dat"); // filter out .dat extension files
            saveFileList = file.list(filenameFilter); // store file names with .dat extension

            if (!file.exists() || Objects.requireNonNull(saveFileList).length == 0) {
                System.out.println("No Save Data Found!\n\t¯\\_(ツ)_/¯");
            } else {
                System.out.println("\nList Of Save Data");
                for (int i = 0; i < saveFileList.length; i++) {
                    System.out.println("[" + i + "] " + saveFileList[i].substring(0, saveFileList[i].lastIndexOf(".")));
                }

                do { // this loop validate user input
                    System.out.print("Enter Save Data Index [0 - " + (saveFileList.length - 1) + "] to Load Save Data: ");
                    while (!scanner.hasNextInt()) {
                        System.out.print("Invalid Input! Try Again.\nEnter Save Data Index (0 - " + saveFileList.length + ") to Load Save Data: ");
                        scanner.next();
                    }
                    saveDataIndex = scanner.nextInt();
                    if ((saveDataIndex < 0) || (saveDataIndex > saveFileList.length)) {
                        System.out.println("Invalid Input! Try Again.");
                    }
                } while ((saveDataIndex < 0) || (saveDataIndex > saveFileList.length));
                System.out.println("File Loading...");

                String savedFileName = "./saveData/" + saveFileList[saveDataIndex]; // concatenate file path with selected file name

                FileInputStream savedDataFile = new FileInputStream(savedFileName); // Create new FileInputStream object and parse SavedFileName string as argument
                ObjectInputStream savedFile = new ObjectInputStream(savedDataFile); // Create new ObjectInputStream object and parse savedDataFile object as argument

                vaccineCount = savedFile.readInt(); // Read vaccine Count from file
                vaccinationBooth = (String[]) (savedFile.readObject()); // Read vaccinationBooth(String[]) array from file
                isEditable = (boolean[]) savedFile.readObject(); // Read isEditable(boolean[]) array from file

                System.out.println("File Loaded Successfully!");
            }
        } catch (Exception e) {
            System.out.println("Oops! Something went Wrong.");
        }
    }

    /**
     * This Method Add Vaccines to Stock
     */
    private static void addVaccinesToStock() {
        while (true) {
            int restock;
            int requiredVaccineCount = 150 - vaccineCount; // calculate required vaccine by subtracting remaining vaccine count from 150 vaccines
            viewRemainingVaccines();
            if (!(vaccineCount == 150)) {
                do { // this loop validate user input
                    System.out.print("Enter Restock Amount or 0 to go back: ");
                    while (!scanner.hasNextInt()) {
                        System.out.print("Invalid Input! Try Again.\nEnter Restock Amount or 0 to go back: ");
                        scanner.next();
                    }
                    restock = scanner.nextInt();
                    if (restock < 0) {
                        System.out.println("Invalid Input! Try Again.");
                    }
                } while (restock < 0);
                if (restock > requiredVaccineCount) {
                    System.out.println("Vaccination Center Store Capacity Overloaded!\nCannot Store More than 150 Vaccines\n");
                } else {
                    vaccineCount += restock;
                    if (restock == 0) {
                        System.out.println("Back to Main Menu...");
                    } else {
                        System.out.println("Stock Update Successful.\nVaccination Count: " + vaccineCount + "\n\n");
                    }
                    break;
                }
            } else {
                System.out.println("Vaccination Center Store Capacity at it's Peak!\n");
                break;
            }
        }
    }

    /**
     * This Method Prints Remaining Vaccine Count
     */
    private static void viewRemainingVaccines() {
        System.out.println("Vaccine Stock Summary");
        int requiredVaccineCount = 150 - vaccineCount;
        System.out.println("Vaccination Center Vaccine Capacity: 150 Vaccines\nVaccines Remaining: " + vaccineCount + " Vaccines\nVaccines Required: " + requiredVaccineCount + " Vaccines");
    }

    /**
     * This Method Prints Warning Message if vaccine Count less than 20
     */
    private static void warningMsg() {
        if (vaccineCount <= 20) {
            String warningMsg = "\t\t******************************************"
                    .concat("\n\t\t*\t\t\t\t Warning!\t\t\t\t *")
                    .concat("\n\t\t*\t\t\t" + vaccineCount + " Vaccines Remaining\t\t *")
                    .concat("\n\t\t******************************************");
            System.out.println(warningMsg);
        }
    }

    /**
     * This Method Check All Booths for Empty or Not
     * if All booths Empty return character 'Y' and All Booths Occupied return character 'N'
     *
     * @return char (' ', ' Y', 'N')
     */
    private static char boothChecker() {
        int trueCount = 0;
        int falseCount = 0;
        char returnChar = ' ';
        for (String s : VaccinationCenter.vaccinationBooth) {
            if (s.equals("*")) {
                trueCount++;
            } else {
                falseCount++;
            }
        }
        if (trueCount == 6) {
            returnChar = 'Y';
        } else if (falseCount == 6) {
            returnChar = 'N';
        }
        return returnChar;
    }

    private static void asciiArt() {
        String art = "\t\t\t█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀"
                .concat("\n\t\t\t█───█─█───█───█───█──█─█▀▄▀█─█──")
                .concat("\n\t\t\t█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀")
                .concat("\n\t\t\t█▄█▄█─█───█───█───█──█─█───█─█──")
                .concat("\n\t\t\t─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀");
        System.out.println(art);
    }
}
