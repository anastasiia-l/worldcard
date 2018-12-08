from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=60)
    DOB = models.DateField('date_of_birth')
    nationality = models.CharField(max_length=60)
    international_passport = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()

class MedicalRecordCard(models.Model):
    customer_id = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    contraindications = models.CharField(max_length=500)
    allergies = models.CharField(max_length=500)
    past_illnesses = models.CharField(max_length=1000)

class Insurer(models.Model):
    insurer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    contacts = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()

class MedicalInstitution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    email = models.EmailField()

class Medic(models.Model):
    medic_id = models.AutoField(primary_key=True)
    institution_id = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    full_name = models.CharField(max_length=60)
    status = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    email = models.EmailField()

class MedicalInsurancePolicy(models.Model):
    policy_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    insurer_id = models.ForeignKey(Insurer, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=80)
    limit = models.DecimalField( max_digits=10, decimal_places=2)
    duration = models.DurationField()
    region = models.CharField(max_length=100)


class Call(models.Model):
    call_id = models.AutoField(primary_key=True)
    policy_id = models.ForeignKey(Insurer, on_delete=models.CASCADE)
    call_type = models.CharField(max_length=80)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dateTime = models.DateTimeField()
    complaint = models.CharField(max_length=500)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    medic_id = models.ForeignKey(Medic, on_delete=models.CASCADE)
    call_id = models.ForeignKey(Call, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=80)
    full_name = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

class Authorization(models.Model):
    email = models.EmailField(primary_key=True)
    hash_password = models.CharField(max_length=280)
