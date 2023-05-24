// SEARCH and SHOW Data
function searchattendance(){
    const attendancetable = document.getElementById('attendance-table');
    const onclickbutton = document.getElementById('from-to-add');
    onclickbutton.style.display ='block';
    const search = document.getElementById('searchid').value;
    if (search === '*') {
        const showGetdata = document.getElementById('get-all-data');
        showGetdata.style.display = "block";
        onclickbutton.style.display = 'none';
        setTimeout(()=>{
            onclickbutton.style.display ='block';
            showGetdata.style.display = "none";
        },1500)
    } else {
        attendancetable.style.display = 'block';
        // pull the data from the API for the specific eid
        fetch(`http://127.0.0.1:5000/attendance?eid=${search}`)
        .then(response => response.json())
        .then(data => {
            const attendanceList = document.getElementById('attendance-list');
            attendanceList.innerHTML = ''; // Clear all data table before adding new data
            data.forEach(attendance=>{
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="text-align:center;">${attendance.eid}</td>
                <td style="text-align:center;">${attendance.date}</td>
                <td style="text-align:center;">${attendance.clock_in}</td>
                <td style="text-align:center;">${attendance.clock_out}</td>
            `;
            attendanceList.appendChild(tr);
            })
            
        })              
        .catch(error => console.error(error));
    }
    }

function checkin(){
    const onclickbutton = document.getElementById('from-to-add');
    const attendancetable = document.getElementById('attendance-table');
    const search = document.getElementById('searchid').value;
    const eidnone = document.getElementById('eid-none');
    const postData ={
        eid:search
    }
        // Set the API endpoint URL
    const apiEndpoint = 'http://127.0.0.1:5000/attendance';

    // Create the request options
    const options = {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    };
    // Send the POST request to the API
    fetch(apiEndpoint, options)
        .then(response => {
        if (response.ok) {
            // Display a success message
            const successMessage = document.getElementById('check-in-success-message');
            successMessage.style.display = 'block';
            attendancetable.style.display = 'none';
            onclickbutton.style.display = 'none';

            setTimeout(() => {
                successMessage.style.display = 'none';
                onclickbutton.style.display = 'block';
                searchattendance();
            }, 1000);
        } else {
            throw new Error('Failed to post data to API.');
        }
        })
        .catch(error => {console.error('Error posting data:', error);
                attendancetable.style.display = 'none';
                // Display the error message to the user
                const errorMessage = document.getElementById('error-message');
                errorMessage.textContent = 'Failed to CHECK IN Choose exist Employee ID, Please!!! ' +'(The main error: ' + error.message +')' ;
                errorMessage.style.display = 'block';
                onclickbutton.style.display = 'none';
                setTimeout(()=>{
                    onclickbutton.style.display = 'block';
                    errorMessage.style.display = 'none';
                    searchattendance();
                },2500);
            });
        }

// check OUT
function checkout(){
    const onclickbutton = document.getElementById('from-to-add');
    const attendancetable = document.getElementById('attendance-table');
    const search = document.getElementById('searchid').value;
    const postData ={
        eid:search
    }
        // Set the API endpoint URL
    const apiEndpoint = 'http://127.0.0.1:5000/attendance';

    // Create the request options
    const options = {
        method: 'PUT',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    };

    // Send the POST request to the API
    fetch(apiEndpoint, options)
        .then(response => {
        if (response.ok) {
            // Display a success message
            const successMessage = document.getElementById('check-out-success-message');
            successMessage.style.display = 'block';
            attendancetable.style.display = 'none';
            onclickbutton.style.display = 'none';

            setTimeout(() => {
                successMessage.style.display = 'none';
                onclickbutton.style.display = 'block';
                searchattendance();
            }, 1000);
        } else {
            throw new Error('Failed to post data to API.');
        }
        })
        .catch(error => {console.error('Error posting data:', error);
                attendancetable.style.display = 'none';
                // Display the error message to the user
                const errorMessage = document.getElementById('error-message');
                errorMessage.textContent = 'Failed to CHECK OUT Choose exist Employee ID, Please!!! ' +'(The main error: ' + error.message +')' ;
                errorMessage.style.display = 'block';
                onclickbutton.style.display = 'none';
                setTimeout(()=>{
                    onclickbutton.style.display = 'block';
                    errorMessage.style.display = 'none';
                    searchattendance();
                },2500);
            });
        }