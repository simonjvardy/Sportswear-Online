/*
    Code adapted from the CI Boutique Ado mini project
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// setup variables
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
let form = document.getElementById('payment-form');

// Prevents the form from submitting disabling the card element
// and triggers the loading overlay
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Capture form data not in the payment intent and
    // instead post to the cache_checkout_data view
    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';

    // Post the Stripe data to the cache_checkout_data view
    $.post(url, postData).done(function () {
        // if payment intent returns 200 response, call confirmCardPayment
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.first_name.value + ' ' + form.last_name.value),
                    phone: $.trim(form.telephone.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.first_name.value + ' ' + form.last_name.value),
                phone: $.trim(form.telephone.value),
                address: {
                    line1: $.trim(form.address_line1.value),
                    line2: $.trim(form.address_line2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                // if there's an error, hide the loading overlay
                // and re-enable the card element and submit button
                let errorDiv = document.getElementById('card-errors');
                let html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                //otherwise if all OK submit the form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // in case of status=400, just reload the page, the error will be in django messages
        location.reload();
    })
});