function searchPayment() {
    const searchid = document.getElementById('searchid').value;
    const searchmonth = document.getElementById('searchmonth').value;
    const searchyear = document.getElementById('searchyear').value;
    const paymenttable = document.getElementById('payment-table');
    fetch(`http://127.0.0.1:5000/payment?eid=${searchid}&month=${searchyear}&year=${searchmonth}`)
        .then(response => response.json())
        .then(payment => {
        paymenttable.style.display = 'block';
        const paymentList = document.getElementById('payment-list');
        paymentList.innerHTML = ''; // Clear all data table before adding new data

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td style="text-align:center;">${payment.eid}</td>
            <td style="text-align:center;">${payment.salary}</td>
        `;
        paymentList.appendChild(tr);
        })
        .catch(error => {
        paymenttable.style.display = 'none';
        console.log('payment not found:', error);
        });}