from typing import List, Dict, Optional

def readPatientsFromFile(fileName):
    patients = {}
    date = ""
    temp = 0.0
    heartRate = 0
    respRate = 0
    systPressure = 0
    diastPressure = 0
    oxySat = 0
    try:
        file = open(fileName, "r")
        for line in file:
            try:
                data = line.strip().split(',')
                if len(data) != 8:
                    raise Exception(f"Invalid number of fields ({len(data)}) in line: {line}")
                date = data[1]
                temp = float(data[2])
                heartRate = int(data[3])
                respRate = int(data[4])
                systPressure = int(data[5])
                diastPressure = int(data[6])
                oxySat = int(data[7])
                if not (35 <= temp <= 42):
                    raise Exception(f'Invalid temperature value ({temp}) in line: {line}')
                if not (30 <= heartRate <= 180):
                    raise Exception(f"Invalid heart rate value ({heartRate}) in line: {line}")
                if not (5 <= respRate <= 40):
                    raise Exception(f"Invalid respiratory rate value ({respRate}) in line: {line}")
                if not (70 <= systPressure <= 200):
                    raise Exception(f"Invalid systolic blood pressure value ({systPressure}) in line: {line}")
                if not (40 <= diastPressure <= 120):
                    raise Exception(f"Invalid diastolic blood pressure value ({diastPressure}) in line: {line}")
                if not (70 <= oxySat <= 100):
                    raise Exception(f"Invalid oxygen saturation value ({oxySat}) in line: {line}")
                visit = [date,temp,heartRate,respRate,systPressure,diastPressure,oxySat]
                patients.setdefault(data[0],[]).append(visit)
            except ValueError:
                print(f'Invalid data type in line: {line}')
            except Exception as error:
                print(error)
                continue 
        return patients
    except IOError:
        print(f'The file {fileName} could not be found.')
    finally:
        file.close()

# Displays patient data for a given patient ID
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    try:
        if patientId == 0:
            for id in patients:
                printPatientData(patients,id)
        elif str(patientId) not in patients.keys():
            raise Exception(f"Patient with ID {patientId} not found.")
        else:
            printPatientData(patients,str(patientId))
    except Exception as error:
        print(error)

# dynamic helper function to extract and print patient history
def printPatientData(patients,patientId):
    visits = patients[patientId]
    print(f'Patient ID: {patientId}')
    for visit in visits:
        print(f' Visit date: {visit[0]}')
        print(f'  Temperature: {visit[1]:.2f} C')
        print(f'  Heart Rate: {visit[2]} bpm')
        print(f'  Respiratory Rate: {visit[3]} bpm')
        print(f'  Systolic Blood Pressure: {visit[4]} mmHg')
        print(f'  Diastolic Blood Pressure: {visit[5]} mmHg')
        print(f'  Oxygen Saturation: {visit[6]} %')
    return

# dislpays the average of each vital sign for all patients or for the specified patient
def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        patientId = int(patientId)
        if not isinstance(patients, dict):
            raise Exception(f"Error: 'patients' should be a dictionary.")
        vitals = []
        temp_sum = 0
        hr_sum = 0
        rr_sum = 0
        sbp_sum = 0
        dbp_sum = 0
        spo2_sum = 0
        num_visits = 0 
        if patientId == 0:
            if not patients:
                raise Exception(f'No data found.')
            for patient in patients:
                vitals = aggregatePatientStats(patients,patient)
                if vitals:
                    num_visits = num_visits + vitals[0]
                    temp_sum = temp_sum + vitals[1]
                    hr_sum = hr_sum + vitals[2]
                    rr_sum = rr_sum + vitals[3]
                    sbp_sum = sbp_sum + vitals[4]
                    dbp_sum = dbp_sum + vitals[5]
                    spo2_sum = spo2_sum + vitals[6]
            print(f'Vital Signs for All Patients:')
            print(f' Average temperature: {(temp_sum/num_visits):.2f} C')
            print(f' Average heart rate: {(hr_sum/num_visits):.2f} bpm')
            print(f' Average respiratory rate: {(rr_sum/num_visits):.2f} bpm')
            print(f' Average systolic blood pressure: {(sbp_sum/num_visits):.2f} mmHg')
            print(f' Average diastolic blood pressure: {(dbp_sum/num_visits):.2f} mmHg')
            print(f' Average oxygen saturation: {(spo2_sum/num_visits):.2f} %')        
        elif str(patientId) not in patients.keys():
            raise Exception(f'No data found for patient with ID {patientId}.')
        else:
            vitals = aggregatePatientStats(patients,str(patientId))
            if vitals:
                print(f'Vital Signs for Patient {patientId}:')
                print(f' Average temperature: {(vitals[1]/vitals[0]):.2f} C')
                print(f' Average heart rate: {(vitals[2]/vitals[0]):.2f} bpm')
                print(f' Average respiratory rate: {(vitals[3]/vitals[0]):.2f} bpm')
                print(f' Average systolic blood pressure: {(vitals[4]/vitals[0]):.2f} mmHg')
                print(f' Average diastolic blood pressure: {(vitals[5]/vitals[0]):.2f} mmHg')
                print(f' Average oxygen saturation: {(vitals[6]/vitals[0]):.2f} %')
            else:
                raise Exception(f'No data found.')
        return
    except ValueError:
        print(f"Error: 'patientId' should be an integer.")
    except Exception as error:
        print(error)

# dynamic helper function that calculate number of visits and sum vitals per patient
def aggregatePatientStats(patients, patientId):
    visits = patients[patientId]
    vitals_sum = []
    temp_sum = 0
    hr_sum = 0
    rr_sum = 0
    sbp_sum = 0
    dbp_sum = 0
    spo2_sum = 0
    num_visits = 0
    for visit in visits:
        #Sum visits
        num_visits += 1
        #Sum Temperature vitals
        temp_sum = temp_sum + visit[1]
        #Sum Heart Rate vitals
        hr_sum = hr_sum + visit[2]
        #Sum Respiratory Rate vitals
        rr_sum = rr_sum + visit[3]
        #Sum Systolic Blood Pressure vitals
        sbp_sum = sbp_sum + visit[4]
        #Sum Diastolic Blood Pressure vitals
        dbp_sum = dbp_sum + visit [5]
        #Sum Oxygen Saturation vitals
        spo2_sum = spo2_sum + visit[6]
    vitals_sum = [num_visits,temp_sum,hr_sum,rr_sum,sbp_sum,dbp_sum,spo2_sum]
    return vitals_sum
        


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    newLinePatientsFile = ""
    visit = []
    try:
         # Verifies if the date is valid
        dateParts = date.split("-")
        if not (len(dateParts) == 3 and len(dateParts[0]) == 4 and len(dateParts[1]) == 2 and len(dateParts[2]) == 2):
            raise Exception(f'Invalid date format. Please enter date in the format "yyyy-mm-dd".')
        year = int(dateParts[0])
        month = int(dateParts[1])
        day = int(dateParts[2])
        if year < 1900:
            raise Exception(f'Invalid date. Please enter a valid date.')
        if month < 1 or month > 12:
            raise Exception(f'Invalid date. Please enter a valid date.')
        if day < 1 or day > 31:
            raise Exception(f'Invalid date. Please enter a valid date.')
        # Verifies if the temp is valid
        if temp < 35.0 or temp > 42.0:
            raise Exception(f'Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.')
        # Verifies if the heart rate is valid
        if hr < 30 or hr > 180:
            raise Exception(f'Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.')
        # Verifies if the respiratory rate is valid
        if rr < 5 or rr > 40:
            raise Exception(f'Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.')
        # Verifies if the systolic blood pressure is valid
        if sbp <70 or sbp > 200:
            raise Exception(f'Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.')
        # Verifies if the diastolic blood pressure is valid
        if dbp < 40 or dbp > 120:
            raise Exception(f'Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.')
        # Verifies if the oxygen saturation level is valid
        if spo2 < 70 or spo2 > 100:
            raise Exception(f'Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.')
        # Converts patient info intro a string so it can be appended into the file
        newLinePatientsFile = f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}"
        visit = [date,temp,hr,rr,sbp,dbp,spo2]
        # Appends the patient info into the file
        with open(fileName, "a") as file:
            file.write("\n")
            file.write(newLinePatientsFile)
        # appends the information into the dictionary
        if patientId in patients:
            patients[patientId].append(visit)
        else:
            patients.setdefault(patientId,[]).append(visit)
        print(f"Visit is saved successfully for Patient #{patientId}")
        return
    except ValueError:
        print(f'Invalid date format. Please enter the date in the format "yyyy-mm-dd".')
    except Exception as error:
        print(error)
    print(patients)

# Finds visit by year, month, or both
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    try:
        if not patients:
            raise Exception([])
        if (year is not None and year < 1900) and (month is None):
            raise Exception([])
        elif (year is not None and year > 1900) and (month is not None and ( month < 1 or month > 12)):
            raise Exception([])
        elif (year is not None and year < 1900) and (month is not None and ( month < 1 or month > 12)):
            raise Exception([])
        elif (year is None) and (month is not None):
            raise Exception([])
        # find the visits of all patients
        if (year is None) and (month is None):
            for patientId, visit in patients.items():  
                for information in visit:
                    info = (patientId,tuple(information))
                    visits.append(info)
        else:
            # finds the vist of patient with specific year and month
            if (year is not None) and (month is not None):
                strYear = str(year)
                if month < 10:
                    strMonth = "0"+str(month)
                else:
                    strMonth = str(month)
                date = strYear + "-" + strMonth
            # finds the visit of patient with specific year only
            elif (year is not None) and (month is None):
                strYear = str(year)
                date = strYear

            for patientId, visit in patients.items():  
                for information in visit:
                    # slices the visit date in the dictionary
                    slicedDateYearMonth = information[0][0:7]
                    slicedDateYear = information[0][0:4]
                    # compares the users picked date with the slice dates in the dictionary and appends the appropriate information
                    if date == slicedDateYearMonth:
                        info = (patientId,tuple(information))
                        visits.append(info)
                    elif date == slicedDateYear:
                        info = (patientId,tuple(information))
                        visits.append(info)
                    else:
                        continue

    except Exception as error:
        print(error)
    return visits
        



# Find patients who need follow-up visits based on abnormal vital signs
def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    for id, visit in patients.items():  
            for information in visit:
                if (information[2] > 100 or information[2] < 60):
                    followup_patients.append(id)
                elif (information[4] > 140):
                    followup_patients.append(id)
                elif (information[5] > 90):
                    followup_patients.append(id)
                elif (information[6] < 90):
                    followup_patients.append(id)
                else:
                    break               
    return followup_patients

# delete all visists of a particular patient
def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    try:
        if (str(patientId) not in patients.keys()):
            raise Exception(f"No data found for patient with ID {patientId}")
        if (str(patientId) in patients.keys()):
            # deletes the id of the patient in the dictionary, as a result the key-value pair is deleted
            del patients[str(patientId)]
        # opens the file to rewrite the whole dictionary into the file    
        with open(filename, "w") as file:
            for id, visits in patients.items():
                for visit in visits:
                    # converts all the patients visit information into a string and separates it by a comma
                    information = ",".join(map(str,visit))
                    # write the file with the id and the visit information for each patientID that has not been deleted
                    file.write(f'{id},{information}\n')
        print(f'Data for patient {patientId} has been deleted')
    except Exception as error:
        print(error)

                    





###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()