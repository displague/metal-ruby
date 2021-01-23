// Code generated by go-swagger; DO NOT EDIT.

package hardware_reservations

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// PostHardwareReservationsIDMoveReader is a Reader for the PostHardwareReservationsIDMove structure.
type PostHardwareReservationsIDMoveReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *PostHardwareReservationsIDMoveReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewPostHardwareReservationsIDMoveCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewPostHardwareReservationsIDMoveUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewPostHardwareReservationsIDMoveForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewPostHardwareReservationsIDMoveNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewPostHardwareReservationsIDMoveCreated creates a PostHardwareReservationsIDMoveCreated with default headers values
func NewPostHardwareReservationsIDMoveCreated() *PostHardwareReservationsIDMoveCreated {
	return &PostHardwareReservationsIDMoveCreated{}
}

/*PostHardwareReservationsIDMoveCreated handles this case with default header values.

ok
*/
type PostHardwareReservationsIDMoveCreated struct {
	Payload *types.HardwareReservation
}

func (o *PostHardwareReservationsIDMoveCreated) Error() string {
	return fmt.Sprintf("[POST /hardware-reservations/{id}/move][%d] postHardwareReservationsIdMoveCreated  %+v", 201, o.Payload)
}

func (o *PostHardwareReservationsIDMoveCreated) GetPayload() *types.HardwareReservation {
	return o.Payload
}

func (o *PostHardwareReservationsIDMoveCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.HardwareReservation)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewPostHardwareReservationsIDMoveUnauthorized creates a PostHardwareReservationsIDMoveUnauthorized with default headers values
func NewPostHardwareReservationsIDMoveUnauthorized() *PostHardwareReservationsIDMoveUnauthorized {
	return &PostHardwareReservationsIDMoveUnauthorized{}
}

/*PostHardwareReservationsIDMoveUnauthorized handles this case with default header values.

unauthorized
*/
type PostHardwareReservationsIDMoveUnauthorized struct {
}

func (o *PostHardwareReservationsIDMoveUnauthorized) Error() string {
	return fmt.Sprintf("[POST /hardware-reservations/{id}/move][%d] postHardwareReservationsIdMoveUnauthorized ", 401)
}

func (o *PostHardwareReservationsIDMoveUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewPostHardwareReservationsIDMoveForbidden creates a PostHardwareReservationsIDMoveForbidden with default headers values
func NewPostHardwareReservationsIDMoveForbidden() *PostHardwareReservationsIDMoveForbidden {
	return &PostHardwareReservationsIDMoveForbidden{}
}

/*PostHardwareReservationsIDMoveForbidden handles this case with default header values.

forbidden
*/
type PostHardwareReservationsIDMoveForbidden struct {
}

func (o *PostHardwareReservationsIDMoveForbidden) Error() string {
	return fmt.Sprintf("[POST /hardware-reservations/{id}/move][%d] postHardwareReservationsIdMoveForbidden ", 403)
}

func (o *PostHardwareReservationsIDMoveForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewPostHardwareReservationsIDMoveNotFound creates a PostHardwareReservationsIDMoveNotFound with default headers values
func NewPostHardwareReservationsIDMoveNotFound() *PostHardwareReservationsIDMoveNotFound {
	return &PostHardwareReservationsIDMoveNotFound{}
}

/*PostHardwareReservationsIDMoveNotFound handles this case with default header values.

not found
*/
type PostHardwareReservationsIDMoveNotFound struct {
}

func (o *PostHardwareReservationsIDMoveNotFound) Error() string {
	return fmt.Sprintf("[POST /hardware-reservations/{id}/move][%d] postHardwareReservationsIdMoveNotFound ", 404)
}

func (o *PostHardwareReservationsIDMoveNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
