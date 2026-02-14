from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    user_roles = relationship("UserRole", back_populates="user")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    user_roles = relationship("UserRole", back_populates="role")

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))

    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")

class BusinessElement(Base):
    __tablename__ = "business_elements"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class AccessRolesRules(Base):
    __tablename__ = "access_roles_rules"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    element_id = Column(Integer, ForeignKey("business_elements.id"))

    read_permission = Column(Boolean, default=False)
    read_all_permission = Column(Boolean, default=False)
    create_permission = Column(Boolean, default=False)
    update_permission = Column(Boolean, default=False)
    update_all_permission = Column(Boolean, default=False)
    delete_permission = Column(Boolean, default=False)
    delete_all_permission = Column(Boolean, default=False)

