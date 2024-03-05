from django.db import models
from employee_app.util.util import get_uuid_id
from django.core.validators import MaxValueValidator,  MinValueValidator

class BaseModel(models.Model):
    id = models.CharField(max_length = 150, editable = False, primary_key = True, default = get_uuid_id)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = models.Manager()


    class Meta:
        abstract = True


class Employee(BaseModel):

    roleChoices = (
        ("MANAGER", "Manager"),
        ("HR MANAGER", "Human Resource Manager"),
        ("DEVELOPER", "Developer"),
    )


    name =models.CharField(max_length = 100)
    address = models.CharField(max_length = 150)
    slug = models.CharField(max_length = 255)
    phone_number = models.PositiveIntegerField(validators = [MaxValueValidator(9999999999), MinValueValidator(9800000000)])
    role = models.CharField(choices = roleChoices, max_length = 255)
    joined_date = models.DateField()




class Projects(BaseModel):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    members = models.ManyToManyField(Employee)
    expected_date_completion = models.DateField()