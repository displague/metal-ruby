// Code generated by go-swagger; DO NOT EDIT.

package connections

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// UpdateVirtualCircuitReader is a Reader for the UpdateVirtualCircuit structure.
type UpdateVirtualCircuitReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *UpdateVirtualCircuitReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewUpdateVirtualCircuitOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 202:
		result := NewUpdateVirtualCircuitAccepted()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewUpdateVirtualCircuitForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewUpdateVirtualCircuitNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewUpdateVirtualCircuitOK creates a UpdateVirtualCircuitOK with default headers values
func NewUpdateVirtualCircuitOK() *UpdateVirtualCircuitOK {
	return &UpdateVirtualCircuitOK{}
}

/*UpdateVirtualCircuitOK handles this case with default header values.

ok
*/
type UpdateVirtualCircuitOK struct {
	Payload *types.VirtualCircuit
}

func (o *UpdateVirtualCircuitOK) Error() string {
	return fmt.Sprintf("[PUT /virtual-circuits/{id}][%d] updateVirtualCircuitOK  %+v", 200, o.Payload)
}

func (o *UpdateVirtualCircuitOK) GetPayload() *types.VirtualCircuit {
	return o.Payload
}

func (o *UpdateVirtualCircuitOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.VirtualCircuit)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateVirtualCircuitAccepted creates a UpdateVirtualCircuitAccepted with default headers values
func NewUpdateVirtualCircuitAccepted() *UpdateVirtualCircuitAccepted {
	return &UpdateVirtualCircuitAccepted{}
}

/*UpdateVirtualCircuitAccepted handles this case with default header values.

accepted
*/
type UpdateVirtualCircuitAccepted struct {
	Payload *types.VirtualCircuit
}

func (o *UpdateVirtualCircuitAccepted) Error() string {
	return fmt.Sprintf("[PUT /virtual-circuits/{id}][%d] updateVirtualCircuitAccepted  %+v", 202, o.Payload)
}

func (o *UpdateVirtualCircuitAccepted) GetPayload() *types.VirtualCircuit {
	return o.Payload
}

func (o *UpdateVirtualCircuitAccepted) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.VirtualCircuit)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateVirtualCircuitForbidden creates a UpdateVirtualCircuitForbidden with default headers values
func NewUpdateVirtualCircuitForbidden() *UpdateVirtualCircuitForbidden {
	return &UpdateVirtualCircuitForbidden{}
}

/*UpdateVirtualCircuitForbidden handles this case with default header values.

forbidden
*/
type UpdateVirtualCircuitForbidden struct {
}

func (o *UpdateVirtualCircuitForbidden) Error() string {
	return fmt.Sprintf("[PUT /virtual-circuits/{id}][%d] updateVirtualCircuitForbidden ", 403)
}

func (o *UpdateVirtualCircuitForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateVirtualCircuitNotFound creates a UpdateVirtualCircuitNotFound with default headers values
func NewUpdateVirtualCircuitNotFound() *UpdateVirtualCircuitNotFound {
	return &UpdateVirtualCircuitNotFound{}
}

/*UpdateVirtualCircuitNotFound handles this case with default header values.

not found
*/
type UpdateVirtualCircuitNotFound struct {
}

func (o *UpdateVirtualCircuitNotFound) Error() string {
	return fmt.Sprintf("[PUT /virtual-circuits/{id}][%d] updateVirtualCircuitNotFound ", 404)
}

func (o *UpdateVirtualCircuitNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
