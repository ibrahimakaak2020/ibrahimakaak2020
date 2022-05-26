from db.database.database import Base , db_engine
from db.models.models import Company_Users , Users , Manufacture , Equipment , Equipment_Model , EquipmentOperation as eqo , Equipment_Type , Location, EquipmentRecieve

from sqlalchemy.orm import Session 
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text , select
session = Session(db_engine)
#qeq_model =text("select e.sn,em.emid ,em.equipment_model  ,et.equipment_type , m.company_name from equipment e,equipment_model em, manufacture m ,equipment_type et where e.emid==em.emid and em.mid==m.mid and em.eid==et.eid")
#qequipment=session.query(Equipment.sn).from_statement(qeq_model).all()
#qequipment = session.query(Users.staffno , Users.staffname, Equipment.sn ,
# Equipment_Model.equipment_model ,Location.loc_name, Location.building, 
#  Location.contact_number , Equipment_Type.equipment_type , Manufacture.company_name 
# , eqo.date_of_send , eqo.send_desc  )
#query = query.join(eqo).join(Users).join(Company_Users).join(Equipment).join(Location).join(Equipment_Model).join(Equipment_Type).join(Manufacture)
#results = qequipment.all()

class Get_Manfacture:
    @classmethod
    def get(self,company_name = None ,company_id = None):
        try:
            if company_name and company_id :
                g_m= session.query(Manufacture).filter(and_(Manufacture.company_name.ilike('%'+company_name+'%'),Manufacture.mid == company_id)).one()
            elif not company_name and company_id:
                 g_m= session.query(Manufacture).filter(Manufacture.mid == company_id).one()
            elif company_name and not  company_id:
                 g_m= session.query(Manufacture).filter(Manufacture.company_name.ilike('%'+company_name+'%') ).all()
                
            else:
                 g_m= session.query(Manufacture).all()
        
        except NoResultFound:
                return None
    
        return g_m



class Get_Equipment_Model:
    @classmethod
    def get(self,equipment_model = None ,model_id = None):
        try:
            if equipment_model and model_id :
                g_m= session.query(Equipment_Model).filter(and_(Equipment_Model.equipment_model.ilike('%'+equipment_model+'%'),Equipment_Model.emid == model_id)).one()
            elif not equipment_model and model_id:
                 g_m= session.query(Equipment_Model).filter(Equipment_Model.emid== model_id).one()
            elif equipment_model and not  model_id:
                 g_m= session.query(Equipment_Model).filter(Equipment_Model.equipment_model.ilike('%'+equipment_model+'%') ).all()
                
            else:
                 g_m= session.query(Equipment_Model).all()
        
        except NoResultFound:
                return None
    
        return g_m
    



class Get_Equipment_Type:
    @classmethod
    def get(self,equipment_type = None ,type_id = None):
        try:
            if equipment_type and type_id :
                g_m= session.query(Equipment_Type).filter(and_(Equipment_Type.equipment_type.ilike('%'+equipment_type+'%'),Equipment_Type.eid == type_id)).one()
            elif not equipment_type and type_id:
                 g_m= session.query(Equipment_Type).filter(Equipment_Type.eid == type_id).one()
            elif equipment_type and not  type_id:
                 g_m= session.query(Equipment_Type).filter(Equipment_Type.equipment_type.ilike('%'+equipment_type+'%') )
                
            else:
                 g_m= session.query(Equipment_Type).all()
        
        except NoResultFound:
                return None
    
        return g_m


class Get_Location:
    @classmethod
    def get(self,location_name = None ,location_id = None):
        try:
            if location_name and location_id :
                g_m= session.query(Location).filter(
                    and_(
                        Location.loc_name.ilike('%'+location_name+'%'),Location.locid == location_id
                        )
                    ).one()
            elif not location_name and location_id:
                 print("name=False and id=True")
                 g_m= session.query(Location).filter(Location.locid == location_id).one()
            elif location_name and not location_id:
                 print("name=True and id=False")
                 g_m= session.query(Location).filter(Location.loc_name.ilike('%'+ location_name +'%') ).all()
                
            else:
                 g_m= session.query(Location).all()
        
        except NoResultFound:
                return None
    
        return g_m
 


class Get_Equipment:
    @classmethod
    def get(self,sn = None ,equipment_model_id = None,location_id = None):
        try:
                if sn and not equipment_model_id  and not location_id  :
                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.sn.ilike('%'+sn+'%'))
                elif not sn and  equipment_model_id  and not location_id  :
                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.emid==equipment_model_id)
                elif not sn and  not equipment_model_id  and  location_id  :

                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.locid  == location_id)
          
                
                else:
                     g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture)
        
        except NoResultFound:
                return None
    
        return g_m

class Get_EquipmentOperation:
    @classmethod
    def get(self,sn = None , = None,location_id = None):
        try:
                if sn and not equipment_model_id  and not location_id  :
                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.sn.ilike('%'+sn+'%'))
                elif not sn and  equipment_model_id  and not location_id  :
                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.emid==equipment_model_id)
                elif not sn and  not equipment_model_id  and  location_id  :

                    g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.locid  == location_id)
          
                
                else:
                     g_m= session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture)
        
        except NoResultFound:
                return None
    
        return g_m

#print(Get_Equipment.get())
#print(Get_Manfacture.get())

#qeq_model =text("select e.sn,em.emid ,em.equipment_model  ,et.equipment_type , m.company_name from equipment e,equipment_model em, manufacture m ,equipment_type et where e.emid==em.emid and em.mid==m.mid and em.eid==et.eid")
#qequipment=session.query(Equipment.sn).from_statement(qeq_model)

#print(session.execute(qeq_model))


eqm=session.query(Equipment_Model,Equipment_Type,Manufacture).join(Equipment_Type,Manufacture).all()

#query1=session.query( Equipment,Equipment_Model,Equipment_Type,Manufacture ,Location).join(Location,Equipment_Model,Equipment_Type,Manufacture).where(Equipment.sn.ilike('%'+sn+'%'))
#print(session.execute(query1).Equipment)

print('{:10}{:20}{:20}{:20}{:10}'.format("sn ","Equipment Model","Equipment Type","Manufacture","location"))
print("-" * 80)
for row  in  Get_Equipment.get():

    print("{:10}{:20} {:20}{:20} {:10}".format(row.Equipment.sn,row.Equipment_Model.equipment_model,row.Equipment_Type.equipment_type,row.Manufacture.company_name,row.Location.loc_name))
    
#         print(row[0].sn,row[1].equipment_model,row[2].equipment_type,row[3].company_name) .join(Equipment_Model,Equipment.emid == Equipment_Model.emid )



 