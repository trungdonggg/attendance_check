
function searchHoliday() {
const search = document.getElementById('searchid').value;
const holidaytable = document.getElementById('holiday-table');

    if (search ==='*'){
    fetch('http://127.0.0.1:5000/holiday?jid=*')
    .then(response => response.json())
    .then(data => {
        holidaytable.style.display = 'block';
        const holidayList = document.getElementById('holiday-list');
        holidayList.innerHTML = ''; // Clear all data table before adding new data
        data.forEach(holiday => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td style="text-align:center;">${holiday.jid}</td>
            <td style="text-align:center;">${holiday.holiday_month}</td>
            <td style="text-align:center;">${holiday.holiday_date}</td>
            <td><button onclick="deleteHoliday('${holiday.jid}','${holiday.holiday_month}','${holiday.holiday_date}')">Delete</button></td>
        `;
        holidayList.appendChild(tr);
        });
    })
    .catch(error => console.error(error));
} else {
    // Fetch holiday by ID from the API
    fetch(`http://127.0.0.1:5000/holiday?jid=${search}`)
    .then(response => response.json())
    .then(holiday => {
        holidaytable.style.display = 'block';
        const holidayList = document.getElementById('holiday-list');
        holidayList.innerHTML = ''; // Clear all data table before adding new data

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td style="text-align:center;">${holiday.jid}</td>
            <td style="text-align:center;">${holiday.holiday_month}</td>
            <td style="text-align:center;">${holiday.holiday_date}</td>
            <td><button onclick="deleteHoliday('${holiday.jid}','${holiday.holiday_month}','${holiday.holiday_date}')">Delete</button></td>
        `;
        holidayList.appendChild(tr);
    })
    .catch(error => {
        holidaytable.style.display = 'none';
        console.log('Holiday not found:', error);
    });
}
}

function showAddForm() {
    const addForm = document.getElementById('form-to-add');
    addForm.style.display = 'block';
}

function deleteHoliday(jid,holidayMonth, holidayDate) {
    const formattedMonth = holidayMonth;
    function getMonthNumberFromName(monthName) {
        return new Date(`${monthName} 1, 2022`).getMonth() + 1;
      }
    const formattedDate = new Number(holidayDate);
    // const formattedMonth = new Date(holidayDate).toISOString().split('T')[0];
    console.log(getMonthNumberFromName(formattedMonth));
    const postData = { jid: jid,holiday_month:getMonthNumberFromName(formattedMonth),holiday_date: formattedDate };

    const options = {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(postData)
    };

    fetch('http://127.0.0.1:5000/holiday', options)
    .then(response => {
        if (response.ok) {
        const successMessage = document.getElementById('delete-success-message');
        successMessage.style.display = 'block';
        const holidaytable = document.getElementById('holiday-table');
        holidaytable.style.display='none';
        setTimeout(() => {
            holidaytable.style.display = 'block';
            successMessage.style.display = 'none';
            searchHoliday(); // Refresh the holiday data after successful deletion
        }, 1000);
        } else {
        throw new Error('Failed to delete data from API.');
        }
    })
    .catch(error => console.error(error));
}

function handleAddFormSubmit(event) {
event.preventDefault();

const form = document.getElementById('form-to-add');
const jid = document.getElementById('jid').value;
const holiday_date = document.getElementById('holiday_date').value;
const holiday_month = document.getElementById('holiday_month').value;

const holidayData = {
    jid: jid,
    holiday_month: holiday_month,
    holiday_date: holiday_date
};

fetch('http://127.0.0.1:5000/holiday?jid=*', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(holidayData)
})
    .then(response => response.json())
    .then(data => {
    const postFormContainer = document.getElementById('form-to-add');
    const holidaytable = document.getElementById('holiday-table');
    const postSuccessMessage = document.getElementById('success-message');
    postSuccessMessage.style.display = 'block';
    holidaytable.style.display = 'none';
    postFormContainer.style.display = 'none';
    form.reset();
    console.log('Data Posted successfully:', data);
    setTimeout(()=>{
        // postFormContainer.style.display = 'none';
        postSuccessMessage.style.display = 'none';
        // // Refresh the holiday list
        searchHoliday();
    },1000)
    })
    .catch(error => {console.error('Error posting data:', error);
                    const postFormContainer = document.getElementById('form-to-add');
                    // Display the error message to the user
                    const errorMessage = document.getElementById('error-message');
                    errorMessage.textContent = 'Failed to post data: ' + error.message;
                    errorMessage.style.display = 'block';
                    postFormContainer.style.display = 'none';
                    const holidaytable = document.getElementById('holiday-table');
                    holidaytable.style.display = 'none';
                    setTimeout(()=>{
                        postFormContainer.style.display = 'block';
                        errorMessage.style.display = 'none';
                        searchHoliday();
                    },1500);
                });
}

// Attach event listeners
document.getElementById('show-form-to-add-holiday').addEventListener('click', showAddForm);
document.getElementById('form-to-add').addEventListener('submit', handleAddFormSubmit);