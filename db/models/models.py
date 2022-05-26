from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from db.database.database import *

from sqlalchemy.orm import relationship


#Base = declarative_base()
class Manufacture(Base):
    __tablename__ = "manufacture"

    mid = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(30),nullable=False)
    equipment_model = relationship("Equipment_Model", back_populates="manufacture")
    def __repr__(self):
       return f"Manufacture(id={self.mid!r}, name={self.company_name})"


class Equipment_Model(Base):
     __tablename__ = "equipment_model" 


     emid=Column(Integer, primary_key=True, index=True)
     equipment_model=Column(String(30),nullable=False) 
     mid=Column(Integer, ForeignKey('manufacture.mid'))
     manufacture = relationship("Manufacture", back_populates="equipment_model")

     eid=Column(Integer, ForeignKey('equipment_type.eid'))
     equipment_type = relationship("Equipment_Type", back_populates="equipment_model")
    
     equipments = relationship("Equipment", back_populates="equipment_model")
     def __repr__(self):
        return f"Equipment Model (id={self.emid!r}, Equipment Model={self.equipment_model!r})"

class Equipment(Base):
    __tablename__ = "equipment"

    sn = Column(String(30), primary_key=True, index=True)
    emid=Column(Integer, ForeignKey('equipment_model.emid') )
    equipment_model = relationship("Equipment_Model", back_populates="equipments")
    locid = Column(Integer,ForeignKey('location.locid'))
    locations = relationship("Location", back_populates="equipments")
    equipmentoperation=relationship("EquipmentOperation", back_populates="equipments")
  
    def __repr__(self):
        return f"Equipment(sn={self.sn!r}, equipment_model={self.equipment_model  !r})"

class Equipment_Type(Base):
    __tablename__ = "equipment_type"

    eid = Column(Integer, primary_key=True, index=True)
    equipment_type = Column(String(30),nullable=False) 
    equipment_model = relationship("Equipment_Model", back_populates="equipment_type")
    def __repr__(self):
        return f"Equipment type (id={self.eid!r}, equipment type={self.equipment_type!r})"



class Location(Base):
    __tablename__ = "location"

    locid = Column(Integer, primary_key=True, index=True)
    loc_name = Column(String(30),nullable=False) 
    building = Column(String(100),nullable=False) 
    contact_number = Column(String(30),nullable=False) 
    equipments= relationship("Equipment", back_populates="locations")
    def __repr__(self):
        return f"Location (id={self.locid!r}, location={self.building!r})"


    
class EquipmentOperation(Base):
    __tablename__ = "equipmentoperation"

    opid = Column(Integer, primary_key=True, index=True)
    date_of_send = Column(DateTime,nullable=False) 
    send_by =  Column(Integer, ForeignKey('users.staffno'))
    user = relationship("User", back_populates="equipment_operation") 
    send_desc = Column(String(30) , nullable=False)
    workorderid=Column(Integer)
    sn = Column(String(30), ForeignKey('equipment.sn'))
    equipments = relationship("Equipment", back_populates="equipmentoperation")
    equipmentrecieved=relationship("EquipmentRecieve", back_populates="equipmentop")
    cid = Column(Integer, ForeignKey("company_users.cid"))
    company_users = relationship("Company_Users", back_populates="send_equipments")
            
    def __repr__(self):
        return f" Equipment operations (SN ={self.sn}, status ={self.equipments})"

class EquipmentRecieve(Base):
    __tablename__ = "equipmentrecieve"
    erid = Column(String(30), primary_key=True, index=True)
    opid= Column(Integer, ForeignKey('equipmentoperation.opid'))
    equipmentop=relationship("EquipmentOperation", back_populates="equipmentrecieved")
    receive_date = Column(DateTime) 
    received_by =  Column(Integer, ForeignKey('users.staffno'))
    local_m=Column(Integer)
    receive_desc = Column(String(30))
    receive_status = Column(Integer)
    billid=Column(String(30))
    billamount=Column(Integer)
    status=Column(Integer)
         
    def __repr__(self):
        return f" Equipment Recieve (SN ={self.erid}, status ={self.status})"



class User(Base):
    __tablename__ = "users"

    staffno = Column(Integer, primary_key=True, index=True)
    staffname = Column(String(100),nullable=False) 
    password = Column(String(30),nullable=False) 
    admin_role=Column(Integer,nullable=False)
    equipment_operation = relationship("EquipmentOperation", back_populates="user")
     
    def __repr__(self):
        return f"User (staff No ={self.staffno  !r}, staff Name={self.staffname !r})"


class Company_Users(Base):
    __tablename__ = "company_users"

    cid = Column(Integer, primary_key=True, index=True)
    name = Column(String(50),nullable=False) 
    company_name_en = Column(String(50),nullable=False) 
    company_name_ar = Column(String(50),nullable=False) 
    contactnumber = Column(String(30),nullable=False) 
    send_equipments = relationship("EquipmentOperation", back_populates="company_users")
    def __repr__(self):
        return f"User (staff No ={self.cid  !r}, staff Name={self.name !r})"
#for test test
