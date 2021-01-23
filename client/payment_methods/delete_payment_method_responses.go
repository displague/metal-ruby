// Code generated by go-swagger; DO NOT EDIT.

package payment_methods

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// DeletePaymentMethodReader is a Reader for the DeletePaymentMethod structure.
type DeletePaymentMethodReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *DeletePaymentMethodReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 204:
		result := NewDeletePaymentMethodNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewDeletePaymentMethodUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewDeletePaymentMethodNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewDeletePaymentMethodNoContent creates a DeletePaymentMethodNoContent with default headers values
func NewDeletePaymentMethodNoContent() *DeletePaymentMethodNoContent {
	return &DeletePaymentMethodNoContent{}
}

/*DeletePaymentMethodNoContent handles this case with default header values.

no content
*/
type DeletePaymentMethodNoContent struct {
}

func (o *DeletePaymentMethodNoContent) Error() string {
	return fmt.Sprintf("[DELETE /payment-methods/{id}][%d] deletePaymentMethodNoContent ", 204)
}

func (o *DeletePaymentMethodNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewDeletePaymentMethodUnauthorized creates a DeletePaymentMethodUnauthorized with default headers values
func NewDeletePaymentMethodUnauthorized() *DeletePaymentMethodUnauthorized {
	return &DeletePaymentMethodUnauthorized{}
}

/*DeletePaymentMethodUnauthorized handles this case with default header values.

unauthorized
*/
type DeletePaymentMethodUnauthorized struct {
}

func (o *DeletePaymentMethodUnauthorized) Error() string {
	return fmt.Sprintf("[DELETE /payment-methods/{id}][%d] deletePaymentMethodUnauthorized ", 401)
}

func (o *DeletePaymentMethodUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewDeletePaymentMethodNotFound creates a DeletePaymentMethodNotFound with default headers values
func NewDeletePaymentMethodNotFound() *DeletePaymentMethodNotFound {
	return &DeletePaymentMethodNotFound{}
}

/*DeletePaymentMethodNotFound handles this case with default header values.

not found
*/
type DeletePaymentMethodNotFound struct {
}

func (o *DeletePaymentMethodNotFound) Error() string {
	return fmt.Sprintf("[DELETE /payment-methods/{id}][%d] deletePaymentMethodNotFound ", 404)
}

func (o *DeletePaymentMethodNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
