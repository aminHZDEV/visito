from app.model.administrator import Administrator
from app.model.appointment import Appointment
from app.model.doctor import Doctor
from app.model.invoice import Invoice
from app.model.medicine import Medicine
from app.model.patient import Patient
from app.model.payment import Payment
from app.model.record import Record
from utils.status import InsertStatus
import datetime

# A flag used to check the state of dummies
is_initiated = False
# Constants
DATE = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
# Constant-ish dummies
DUMMY_ADMINISTRATOR = None
DUMMY_APPOINTMENT = None
DUMMY_DOCTOR = None
DUMMY_INVOICE = None
DUMMY_MEDICINE = None
DUMMY_PATIENT = None
DUMMY_PAYMENT = None
DUMMY_RECORD = None


def initiate():
    global is_initiated
    global DUMMY_ADMINISTRATOR
    global DUMMY_APPOINTMENT
    global DUMMY_DOCTOR
    global DUMMY_INVOICE
    global DUMMY_MEDICINE
    global DUMMY_PATIENT
    global DUMMY_RECORD
    global DUMMY_PAYMENT
    
    # Patient
    DUMMY_PATIENT = Patient.make_dummy()
    status = DUMMY_PATIENT.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy patient. Status: {status}')
    
    # Doctor
    DUMMY_DOCTOR = Doctor.make_dummy()
    status = DUMMY_DOCTOR.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy doctor. Status: {status}')
    
    # Admin
    DUMMY_ADMINISTRATOR = Administrator.make_dummy()
    status = DUMMY_ADMINISTRATOR.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy administrator. Status: {status}')
    
    # Medicine
    DUMMY_MEDICINE = Medicine.make_dummy()
    status = DUMMY_MEDICINE.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy medicine. Status: {status}')

    # Appointment
    DUMMY_APPOINTMENT = Appointment(patient=DUMMY_PATIENT,
                                    doctor=DUMMY_DOCTOR,
                                    date=DATE.strftime('%Y-%m-%d %I:%M %p'))
    status = DUMMY_APPOINTMENT.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy appointment. Status: {status}')

    # Record
    DUMMY_RECORD = Record(patient=DUMMY_PATIENT,
                          token='xxxxxxxxx',
                          info='You are Dummified',
                          date=DATE.strftime('%Y-%m-%d %I:%M %p'))
    status = DUMMY_RECORD.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy medical record. Status: {status}')

    # Payment
    DUMMY_PAYMENT = Payment(amount=111,
                            invoice_number='INV-XXXX',
                            date=DATE.strftime('%Y-%m-%d %I:%M %p'))
    status = DUMMY_PAYMENT.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy payment. Status: {status}')

    # Invoice
    DUMMY_INVOICE = Invoice(patient=DUMMY_PATIENT,
                            service='Dummification',
                            amount=999,
                            invoice_number='INV-XXXX',
                            payments=[DUMMY_PAYMENT])
    status = DUMMY_INVOICE.add(update=False)
    if not (status is InsertStatus.INSERTED_SUCCESSFULLY or status is InsertStatus.DUPLICATE_ENTRY):
        raise RuntimeError(f'Something went wrong while creating dummy administrator. Status: {status}')

    # Set the initiated flag
    is_initiated = True


if not is_initiated:
    initiate()
