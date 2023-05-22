// SEARCH and SHOW Data
function searchattendance(){
const search = document.getElementById('searchid').value;
if (search === '*') {
    const showGetdata = document.getElementById('get-all-data');
    showGetdata.style.display = "block";
    setTimeout(()=>{
    showGetdata.style.display = "none";
    },2500)
} else {
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
const search = document.getElementById('searchid').value;
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

        const successMessage = document.getElementById('success-message');
        successMessage.style.display = 'block';
        setTimeout(() => {
        successMessage.style.display = 'none';
        }, 2500);
    } else {
        throw new Error('Failed to post data to API.');
    }
    })
    .catch(error => {
    console.error(error);
    // Handle errors that occurred during the request
    });
    }

// check OUT
function checkout(){
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
        const successMessage = document.getElementById('success-message');
        successMessage.style.display = 'block';
        setTimeout(() => {
        successMessage.style.display = 'none';
        }, 2500);
    } else {
        throw new Error('Failed to post data to API.');
    }
    })
    .catch(error => {
    console.error(error);
    // Handle errors that occurred during the request
    });
    }