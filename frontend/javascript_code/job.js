let rememberdjobID = ""; // Variable to store the remembered job ID

    function searchJob() {
      const search = document.getElementById('searchid').value;
      const jobtable = document.getElementById('job-table');

      if (search === '*') {
        // Fetch all jobs from the API
        fetch('http://127.0.0.1:5000/job?jid=*')
          .then(response => response.json())
          .then(data => {
            jobtable.style.display = 'block';
            const jobList = document.getElementById('job-list');
            jobList.innerHTML = ''; // Clear all data table before adding new data
            data.forEach(job => {
              const tr = document.createElement('tr');
              tr.innerHTML = `
                <td style="text-align:center;">${job.jid}</td>
                <td style="text-align:center;">${job.title}</td>
                <td style="text-align:center;">${job.based_salary}</td>
                <td style="text-align:center;">${job.from_hour}</td>
                <td style="text-align:center;">${job.to_hour}</td>
                <td style="text-align:center;">${job.late_coefficient}</td>
                <td style="text-align:center;">${job.overtime_coefficient}</td>
                <td style="text-align:center;"><button onclick="showEditForm('${job.jid}')">Edit</button><button data-jid="${job.jid}">Delete</button></td>
              `;
              jobList.appendChild(tr);
            });
          });
      } else {
        // Fetch job by ID from the API
        fetch(`http://127.0.0.1:5000/job?jid=${search}`)
          .then(response => response.json())
          .then(job => {
            jobtable.style.display = 'block';
            const jobList = document.getElementById('job-list');
            jobList.innerHTML = ''; // Clear all data table before adding new data

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="text-align:center;">${job.jid}</td>
                <td style="text-align:center;">${job.title}</td>
                <td style="text-align:center;">${job.based_salary}</td>
                <td style="text-align:center;">${job.from_hour}</td>
                <td style="text-align:center;">${job.to_hour}</td>
                <td style="text-align:center;">${job.late_coefficient}</td>
                <td style="text-align:center;">${job.overtime_coefficient}</td>
                <td style="text-align:center;"><button onclick="showEditForm('${job.jid}')">Edit</button><button data-jid="${job.jid}">Delete</button></td>
              `;
              jobList.appendChild(tr);
          })
          .catch(error => {
            jobtable.style.display = 'none';
            console.log('Job not found:', error);
          });
      }
    }

    function showAddForm() {
      const addForm = document.getElementById('form-to-add');
      addForm.style.display = 'block';
    }

    function showEditForm(jobID) {
        const editFormContainer = document.getElementById('edit-form-container');
        const formToPut = document.getElementById('form_to_put');
        formToPut.style.display = 'block';

        const titleInput = document.getElementById('titleput');
        const basedsalaryInput = document.getElementById('based_salary_put');
        const fromhourInput = document.getElementById('from_hour_put');
        const tohourInput = document.getElementById('to_hour_put');
        const latecoefficientInput = document.getElementById('late_coefficient_put');
        const overtimecoefficientInput = document.getElementById('overtime_coefficient_put');

      // Set the job ID in the edit form
      formToPut.setAttribute('data-job-id', jobID);

      // Fetch job data by ID from the API
      fetch(`http://127.0.0.1:5000/job?jid=${jobID}`)
        .then(response => response.json())
        .then(job => {
            titleInput.value = job.title;
            basedsalaryInput.value = job.based_salary;
            fromhourInput.value = job.from_hour;
            tohourInput.value = job.to_hour;
            latecoefficientInput.value = job.late_coefficient;
            overtimecoefficientInput.value = job.overtime_coefficient;
            editFormContainer.style.display = 'block';
        });
        
      // Store the jobID in the rememberdjobID variable
      rememberdjobID = jobID;
    }

         // Delete data
         function deleteJob(jid) {
        // Send a DELETE request to the API with the jid value
        fetch(`http://127.0.0.1:5000/job`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({jid: jid})
        })
        .then(response => {
          // If the request is successful, remove the corresponding table row
          const row = document.querySelector(`#job-list tr[data-jid="${jid}"]`);
          row.parentNode.removeChild(row);
          const successMessage = document.getElementById('delete-success-message');
          successMessage.style.display = 'block';
        })
        .catch(error => console.error(error));
      }

      // Add an event listener to the job list table
      const jobList = document.getElementById('job-list');
      jobList.addEventListener('click', (event) => {
        const target = event.target;
        // Check if the clicked element is a delete button
        if (target.tagName === 'BUTTON' && target.textContent === 'Delete') {
          const jid = target.getAttribute('data-jid');
          deleteJob(jid);
          const successMessage = document.getElementById('delete-success-message');
          successMessage.style.display = 'block';
          const jobtable = document.getElementById('job-table');
          jobtable.style.display = 'none';
          setTimeout(() => {
            successMessage.style.display = 'none';
            searchJob();
          }, 1000);
        }
      });
    function handleAddFormSubmit(event) {
      event.preventDefault();

        const form = document.getElementById('form-to-add');
        form.style.display = 'block';
        const jid = document.getElementById('jid').value;
        const title = document.getElementById('title').value;
        const basedsalary = document.getElementById('based_salary').value;
        const fromhour = document.getElementById('from_hour').value;
        const tohour = document.getElementById('to_hour').value;
        const latecoefficient = document.getElementById('late_coefficient').value;
        const overtimecoefficient = document.getElementById('overtime_coefficient').value;

      const jobData = {
        jid: jid,
        title: title,
        based_salary: basedsalary,
        from_hour: fromhour,
        to_hour:tohour,
        late_coefficient:latecoefficient,
        overtime_coefficient:overtimecoefficient
    };

      fetch('http://127.0.0.1:5000/job?jid=*', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(jobData)
      })
        .then(response => response.json())
        .then(data => {
          const postFormContainer = document.getElementById('form-to-add');
          const jobtable = document.getElementById('job-table');
          const postSuccessMessage = document.getElementById('success-message');
          postSuccessMessage.style.display = 'block';
          jobtable.style.display = 'none';
          postFormContainer.style.display = 'none';
          form.reset();
          console.log('Data Posted successfully:', data);
          setTimeout(()=>{
            // postFormContainer.style.display = 'none';
            postSuccessMessage.style.display = 'none';
            // // Refresh the job list
            searchJob();
          },1000)
        })
        .catch(error => {console.error('Error posting data:', error);
                    const postFormContainer = document.getElementById('form-to-add');
                    // Display the error message to the user
                    const errorMessage = document.getElementById('error-message');
                    errorMessage.textContent = 'Failed to POST Add exist Job ID and Job ID, Please!!! ' +'(The main error: ' + error.message +')' ;
                    errorMessage.style.display = 'block';
                    postFormContainer.style.display = 'none';
                    const jobtable = document.getElementById('job-table');
                    jobtable.style.display = 'none';
                    setTimeout(()=>{
                        postFormContainer.style.display = 'block';
                        errorMessage.style.display = 'none';
                        searchJob();
                    },2000);
                });
    }

function cancelForm() {
  const addForm = document.getElementById('form-to-add');
  addForm.style.display = 'none';
}


    function handlePutFormSubmit(event) {
      event.preventDefault();

        const form = document.getElementById('form_to_put');
        const jobID = form.getAttribute('data-job-id');

        const title = document.getElementById('titleput').value;
        const based_salary = document.getElementById('based_salary_put').value;
        const from_hour = document.getElementById('from_hour_put').value;
        const to_hour = document.getElementById('to_hour_put').value;
        const late_coefficient = document.getElementById('late_coefficient_put').value;
        const overtime_coefficient = document.getElementById('overtime_coefficient_put').value;

      const jobData = {
        jid: jobID,
        title: title,
        basedsalary: based_salary,
        fromhour: from_hour,
        tohour:to_hour,
        latecoefficient:late_coefficient,
        overtimecoefficient:overtime_coefficient
      };

      fetch(`http://127.0.0.1:5000/job`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(jobData)
      })
        .then(response => response.json())
        .then(data => { 
            const editFormContainer = document.getElementById('edit-form-container');
          const jobtable = document.getElementById('job-table');
          const putSuccessMessage = document.getElementById('put-success-message');
          putSuccessMessage.style.display = 'block';
          jobtable.style.display = 'none';
          editFormContainer.style.display = 'none';
          form.reset();
          console.log('Data updated successfully:', data);
          setTimeout(()=>{
            editFormContainer.style.display = 'none';
            putSuccessMessage.style.display = 'none';
            // Refresh the job list
            searchJob();
          },1000)

        })
        .catch(error => console.error('Error updating data:', error));
    }
    function cancelFormedit() {
      const editForm = document.getElementById('form_to_put');
      editForm.style.display = 'none';
    }


    // Attach event listeners
    document.getElementById('show-form-to-add-job').addEventListener('click', showAddForm);
    document.getElementById('form-to-add').addEventListener('submit', handleAddFormSubmit);
    document.getElementById('form_to_put').addEventListener('submit', handlePutFormSubmit);