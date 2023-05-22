let rememberedEmployeeId = ""; // Variable to store the remembered employee ID

    function searchEmployee() {
      const search = document.getElementById('searchid').value;
      const employeetable = document.getElementById('employee-table');

      if (search === '*') {
        // Fetch all employees from the API
        fetch('http://127.0.0.1:5000/employee?eid=*')
          .then(response => response.json())
          .then(data => {
            employeetable.style.display = 'block';
            const employeeList = document.getElementById('employee-list');
            employeeList.innerHTML = ''; // Clear all data table before adding new data

            data.forEach(employee => {
              const tr = document.createElement('tr');
              tr.innerHTML = `
                <td>${employee.eid}</td>
                <td>${employee.name}</td>
                <td>${employee.phone}</td>
                <td>${employee.email}</td>
                <td>
                  <button onclick="showEditForm('${employee.eid}')">Edit</button>
                  <button data-eid="${employee.eid}">Delete</button></td>
                </td>
              `;
              employeeList.appendChild(tr);
            });
          });
      } else {
        // Fetch employee by ID from the API
        fetch(`http://127.0.0.1:5000/employee?eid=${search}`)
          .then(response => response.json())
          .then(employee => {
            employeetable.style.display = 'block';
            const employeeList = document.getElementById('employee-list');
            employeeList.innerHTML = ''; // Clear all data table before adding new data

            const tr = document.createElement('tr');
            tr.innerHTML = `
              <td>${employee.eid}</td>
              <td>${employee.name}</td>
              <td>${employee.phone}</td>
              <td>${employee.email}</td>
              <td>
                <button onclick="showEditForm('${employee.eid}')">Edit</button>
                <button onclick="deleteEmployee('${employee.eid}')">Delete</button>
              </td>
            `;
            employeeList.appendChild(tr);
          })
          .catch(error => {
            employeetable.style.display = 'none';
            console.log('Employee not found:', error);
          });
      }
    }

    function showAddForm() {
      const addForm = document.getElementById('form-to-add');
      addForm.style.display = 'block';
    }

    function showEditForm(employeeId) {
      const editFormContainer = document.getElementById('edit-form-container');
      const formToPut = document.getElementById('form_to_put');

      const namePut = document.getElementById('nameput');
      const phonePut = document.getElementById('phoneput');
      const emailPut = document.getElementById('emailput');

      // Set the employee ID in the edit form
      formToPut.setAttribute('data-employee-id', employeeId);

      // Fetch employee data by ID from the API
      fetch(`http://127.0.0.1:5000/employee?eid=${employeeId}`)
        .then(response => response.json())
        .then(employee => {
          namePut.value = employee.name;
          phonePut.value = employee.phone;
          emailPut.value = employee.email;
          editFormContainer.style.display = 'block';
        });

      // Store the employeeId in the rememberedEmployeeId variable
      rememberedEmployeeId = employeeId;
    }

         // Delete data
         function deleteEmployee(eid) {
        // Send a DELETE request to the API with the eid value
        fetch(`http://127.0.0.1:5000/employee`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({eid: eid})
        })
        .then(response => {
          // If the request is successful, remove the corresponding table row
          const row = document.querySelector(`#employee-list tr[data-eid="${eid}"]`);
          row.parentNode.removeChild(row);
          const successMessage = document.getElementById('delete-success-message');
          successMessage.style.display = 'block';
        })
        .catch(error => console.error(error));
      }

      // Add an event listener to the employee list table
      const employeeList = document.getElementById('employee-list');
      employeeList.addEventListener('click', (event) => {
        const target = event.target;
        // Check if the clicked element is a delete button
        if (target.tagName === 'BUTTON' && target.textContent === 'Delete') {
          const eid = target.getAttribute('data-eid');
          deleteEmployee(eid);
          const successMessage = document.getElementById('delete-success-message');
          successMessage.style.display = 'block';
          const employeetable = document.getElementById('employee-table');
          employeetable.style.display = 'none';
          setTimeout(() => {
            successMessage.style.display = 'none';
            searchEmployee();
          }, 2000);
        }
      });
    function handleAddFormSubmit(event) {
      event.preventDefault();

      const form = document.getElementById('form-to-add');
      const eid = document.getElementById('eid').value;
      const name = document.getElementById('name').value;
      const phone = document.getElementById('phone').value;
      const email = document.getElementById('email').value;

      const employeeData = {
        eid: eid,
        name: name,
        phone: phone,
        email: email
      };

      fetch('http://127.0.0.1:5000/employee?eid=*', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(employeeData)
      })
        .then(response => response.json())
        .then(data => {
          const postFormContainer = document.getElementById('form-to-add');
          const employeetable = document.getElementById('employee-table');
          const postSuccessMessage = document.getElementById('success-message');
          postSuccessMessage.style.display = 'block';
          employeetable.style.display = 'none';
          postFormContainer.style.display = 'none';
          form.reset();
          console.log('Data Posted successfully:', data);
          setTimeout(()=>{
            // postFormContainer.style.display = 'none';
            postSuccessMessage.style.display = 'none';
            // // Refresh the employee list
            searchEmployee();
          },1000)
        })
        .catch(error => console.error('Error posting data:', error));
    }

    function handlePutFormSubmit(event) {
      event.preventDefault();

      const form = document.getElementById('form_to_put');
      const employeeId = form.getAttribute('data-employee-id');
      const name = document.getElementById('nameput').value;
      const phone = document.getElementById('phoneput').value;
      const email = document.getElementById('emailput').value;

      const employeeData = {
        eid:employeeId,
        name: name,
        phone: phone,
        email: email
      };

      fetch(`http://127.0.0.1:5000/employee`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(employeeData)
      })
        .then(response => response.json())
        .then(data => {
          const editFormContainer = document.getElementById('edit-form-container');
          const employeetable = document.getElementById('employee-table');
          const putSuccessMessage = document.getElementById('put-success-message');
          putSuccessMessage.style.display = 'block';
          employeetable.style.display = 'none';
          editFormContainer.style.display = 'none';
          form.reset();
          console.log('Data updated successfully:', data);
          setTimeout(()=>{
            editFormContainer.style.display = 'none';
            putSuccessMessage.style.display = 'none';
            // Refresh the employee list
            searchEmployee();
          },1000)

        })
        .catch(error => console.error('Error updating data:', error));
    }

    // Attach event listeners
    document.getElementById('show-form-to-add-employee').addEventListener('click', showAddForm);
    document.getElementById('form-to-add').addEventListener('submit', handleAddFormSubmit);
    document.getElementById('form_to_put').addEventListener('submit', handlePutFormSubmit);