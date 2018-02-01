from flask import abort,flash,redirect,render_template,url_for
from flask_login import current_user,login_required

from . import admin
from forms import DepartmentForm,RoleForm
from .. import db
from ..models import Department,Role

def check_admin():
	"""
	prevent non-admins from accessing the page

	"""
	if not current_user.is_admin:
		abort(403)

  #Department Views
@admin.route('/departments', methods = ['GET','POST'])
@login_required
def list_departments():
 	 """
     list all the departments

     """
 	 check_admin()

    #check all the departments   in the database and assign them to a variable.departments 
 	 departments = Department.query.all()

 	 return render_template('admin/departments/departments.html',departments = departments,title = "Departments")

@admin.route('/departments/add', methods=['GET','POST'])
@login_required
def add_department():
	"""add a department to the database """
	check_admin()

	add_department = True

	form = DepartmentForm()
	if form.validate_on_submit():
		department = Department(name=form.name.data,description=form.description.data)

		try:
			#add department to the database
			db.session.add(department)
			db.session.commit()
			flash("You have successsfully added a new department.")
		except:
			#incase the department already exists
			flash("Error: department already exists.")
	#once the admin creates a new department,they will be redirected to the departments page
	return render_template('admin/departments/department.html',action="Add", add_department= add_department,form=form,title = "Add Department")

@admin.route('/departments/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_department(id):
		"""Edit department"""
		check_admin()

		add_department = False
        
        #query for the department with the specified id,if it does not exist throw a 404 error
		department = Department.query.get_or_404(id)
		form = DepartmentForm(obj=department)
		if form.validate_on_submit():
			#update the form
			department.name = form.name.data
			department.description = form.description.data
			db.session.commit()
			flash("You have succesfuly edited the department")

            #redirect to the departments page
			return redirect(url_for('admin.list_departments'))

                form.description.data = department.description
                form.name.data = department.name
                return render_template('admin/departments/department.html',action = "Edit",add_department=add_department,form = form,title = "Edit Department")

@admin.route('/departments/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_department(id):
	"""delete department"""
	check_admin()

	add_department = False

	department = Department.query.get_or_404(id)
	db.session.delete(department)
	db.session.commit()
	flash("You have successfully deleted the department")

	#redirect to the admin's page
	return redirect(url_for('admin.list_departments'))

	return render_template(title = "Delete_department")

#role views
@admin.route('/roles')
@login_required
def list_roles():
	check_admin()
	"""list all roles"""
	roles = Role.query.all()
	return render_template('/admin/roles/roles.html', roles = roles ,title= 'Roles')

@admin.route('/roles/add', methods=['GET','POST'])
@login_required
def add_role():
	"""Add role to the database"""
	check_admin()
	add_role = True

	form = RoleForm()
	if form.validate_on_submit():
		role= Role(name= form.name.data,description=form.description.data)

		try:
			#add role to the database 
			db.session.add(role)
			db.session.commit()
			flash('You have successfully added a new role ')
		except:
			#incase the role already exists
		   flash("Error:the role already exists")

		#redirect to the roles page
		return redirect(url_for('admin.list_roles'))

		#load the role template
	return render_template('admin/roles/role.html', add_role=add_role, form = form,title='Add Role')

@admin.route('/roles/edit/<int:id>', methods = ['GET','POST'])
@login_required
def edit_role(id):
  """Edit a role"""
  check_admin()

  add_role = False

  role = Role.query.get_or_404(id)
  form = RoleForm(obj=role)
  if form.validate_on_submit():
	  	role.name = form.name.data
	  	role.description = form.description.data
	  	db.session.add(role)
	  	db.session.commit()
	  	flash('You have successfully edited the role')

	  	#redirect to the roles page
	  	return redirect(url_for('admin.list_roles'))

  form.description.data = role.description 
  form.name.data = role.name
  return render_template('admin/roles/role.html', add_role=add_role,form=form,title="Edit Role")

@admin.route('/roles/delete/<int:id>', methods = ['GET','POST'])
@login_required
def delete_role(id):
	"""Delete a role from the database"""
	check_admin()
	role = Role.query.get_or_404(id)
	db.session.delete(role)
	db.session.commit()
	flash("You have successfully deleted the role from the database")

	#redirect to the roles page
	return redirect(url_for('admin.list_roles'))

	return render_template(title = "Delete Role")






