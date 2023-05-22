
function searchPosition() {
const search = document.getElementById('searchid').value;
const positiontable = document.getElementById('position-table');

if (search === '*') {
    // Fetch all positions from the API
    fetch('http://127.0.0.1:5000/position?eid=*')
    .then(response => response.json())
    .then(data => {
        positiontable.style.display = 'block';
        const positionList = document.getElementById('position-list');
        positionList.innerHTML = ''; // Clear all data table before adding new data

        data.forEach(position => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${position.eid}</td>
            <td>${position.jid}</td>
            <td>${position.from_date}</td>
            <td>
            <button data-eid="${position.eid}">Delete</button></td>
            </td>
        `;
        positionList.appendChild(tr);
        });
    });
} else {
    // Fetch position by ID from the API
    fetch(`http://127.0.0.1:5000/position?eid=${search}`)
    .then(response => response.json())
    .then(position => {
        positiontable.style.display = 'block';
        const positionList = document.getElementById('position-list');
        positionList.innerHTML = ''; // Clear all data table before adding new data

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${position.eid}</td>
            <td>${position.jid}</td>
            <td>${position.from_date}</td>
            <td>
            <button data-eid="${position.eid}">Delete</button></td>
            </td>
        `;
        positionList.appendChild(tr);
    })
    .catch(error => {
        positiontable.style.display = 'none';
        console.log('Position not found:', error);
    });
}
}

function showAddForm() {
const addForm = document.getElementById('form-to-add');
addForm.style.display = 'block';
}


// Delete data
function deletePosition(eid) {
    console.log(eid);
    // Send a DELETE request to the API with the eid value
    fetch(`http://127.0.0.1:5000/position`, {
        method: 'DELETE',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({eid: eid})
    })
    .then(response => {
        // If the request is successful, remove the corresponding table row
        const row = document.querySelector(`#position-list tr[data-eid="${eid}"]`);
        row.parentNode.removeChild(row);
        const successMessage = document.getElementById('delete-success-message');
        successMessage.style.display = 'block';
    })
    .catch(error => console.error(error));
    }

    // Add an event listener to the position list table
    const positionList = document.getElementById('position-list');
    positionList.addEventListener('click', (event) => {
    const target = event.target;
    // Check if the clicked element is a delete button
    if (target.tagName === 'BUTTON' && target.textContent === 'Delete') {
        const eid = target.getAttribute('data-eid');
        deletePosition(eid);
        const successMessage = document.getElementById('delete-success-message');
        successMessage.style.display = 'block';
        const positiontable = document.getElementById('position-table');
        positiontable.style.display = 'none';
        setTimeout(() => {
        successMessage.style.display = 'none';
        searchPosition();
        }, 1000);
    }
    });
function handleAddFormSubmit(event) {
    event.preventDefault();

    const form = document.getElementById('form-to-add');
    const eid = document.getElementById('eid').value;
    const jid = document.getElementById('jid').value;
    const from_date = document.getElementById('from_date').value;


    const positionData = {
    eid: eid,
    jid: jid,
    from_date: from_date,
    };

    fetch('http://127.0.0.1:5000/position?eid=*', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(positionData)
    })
    .then(response => response.json())
    .then(data => {
        const postFormContainer = document.getElementById('form-to-add');
        const positiontable = document.getElementById('position-table');
        const postSuccessMessage = document.getElementById('success-message');
        postSuccessMessage.style.display = 'block';
        positiontable.style.display = 'none';
        postFormContainer.style.display = 'none';
        form.reset();
        console.log('Data Posted successfully:', data);
        setTimeout(()=>{
        // postFormContainer.style.display = 'none';
        postSuccessMessage.style.display = 'none';
        // // Refresh the position list
        searchPosition();
        },1000)
    })
    .catch(error => console.error('Error posting data:', error));
}

// Attach event listeners
document.getElementById('show-form-to-add-position').addEventListener('click', showAddForm);
document.getElementById('form-to-add').addEventListener('submit', handleAddFormSubmit);