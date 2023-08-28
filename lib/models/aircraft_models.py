from sqlalchemy.orm import declarative_base , relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

#Aircraft fleet description
class Aircraft(Base):
    __tablename__ = 'Aircraft'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    body_type = Column(String)

    def __repr__(self):
        return f"\n<Aircraft" \
            + f"id={self.id}, " \
            + f"make={self.make}, " \
            + f"model={self.model}, " \
            + f"body_type={self.body_type} " \
            + ">"

#Air Transportation Association (ATA) chapter numbers and tasks 
class Aircraft_Tasks(Base):
    __tablename__ = 'Maintenance_tasks'
    
    id = Column(Integer, primary_key=True)
    ata_chapter_number = Column(Integer)
    ata_chapter_name = Column(String)
    task = Column(String)

    def __repr__(self):
        return f"\n<Aircraft_Tasks " \
            + f"id={self.id}, " \
            + f"ata_chapter_number={self.ata_chapter_number}, " \
            + f"ata_chapter_name={self.ata_chapter_name}, " \
            + f"task={self.task} " \
            + ">"

