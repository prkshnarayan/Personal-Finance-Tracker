$(document).ready(function() {
    $('#transaction-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "{% url 'home' %}",
            data: $(this).serialize(),
            success: function(response) {
                $('#income').text('Income: $' + response.income);
                $('#expense').text('Expense: $' + response.expense);
                $('#balance').text('Balance: $' + response.balance);

                let t = response.new_transaction;
                $('#transaction-list').prepend(`<li>${t.Date}: ${t.Title} - ${t.Type} - $${t.Amount} - ${t.Category}</li>`);

                $('#transaction-form')[0].reset();
            },
            error: function() {
                alert('Error adding transaction.');
            }
        });
    });
});