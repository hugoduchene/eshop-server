from rest_framework.views import APIView
from rest_framework.response import Response

import stripe

stripe.api_key = 'sk_test_51Ha0TVD5ubqQB5X3MPI1RK2L9VqdrxCl1J66DgYl6HR9OuWtKFrtqtcIhGhQok05vS6M2qTgtRslbbkOmIZFnKvL00RwQef8Yi'


class ChargeViews(APIView):
    def post(self, request, format=None):
        checkout_session = stripe.checkout.Session.create(
            success_url='http://localhost:3000/',
            cancel_url='http://localhost:3000/',
            payment_method_types=['card', "bancontact"],
            mode='payment',
            line_items=request.data,
        )

        return Response(checkout_session.id)


class WebHooksViews(APIView):
    def post(self, request, format=None):
        print(request.data)

        return Response("ahah")
