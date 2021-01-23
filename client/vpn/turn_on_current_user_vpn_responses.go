// Code generated by go-swagger; DO NOT EDIT.

package vpn

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// TurnOnCurrentUserVPNReader is a Reader for the TurnOnCurrentUserVPN structure.
type TurnOnCurrentUserVPNReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *TurnOnCurrentUserVPNReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewTurnOnCurrentUserVPNCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewTurnOnCurrentUserVPNUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewTurnOnCurrentUserVPNUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewTurnOnCurrentUserVPNCreated creates a TurnOnCurrentUserVPNCreated with default headers values
func NewTurnOnCurrentUserVPNCreated() *TurnOnCurrentUserVPNCreated {
	return &TurnOnCurrentUserVPNCreated{}
}

/*TurnOnCurrentUserVPNCreated handles this case with default header values.

created
*/
type TurnOnCurrentUserVPNCreated struct {
}

func (o *TurnOnCurrentUserVPNCreated) Error() string {
	return fmt.Sprintf("[POST /user/vpn][%d] turnOnCurrentUserVpnCreated ", 201)
}

func (o *TurnOnCurrentUserVPNCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewTurnOnCurrentUserVPNUnauthorized creates a TurnOnCurrentUserVPNUnauthorized with default headers values
func NewTurnOnCurrentUserVPNUnauthorized() *TurnOnCurrentUserVPNUnauthorized {
	return &TurnOnCurrentUserVPNUnauthorized{}
}

/*TurnOnCurrentUserVPNUnauthorized handles this case with default header values.

unauthorized
*/
type TurnOnCurrentUserVPNUnauthorized struct {
}

func (o *TurnOnCurrentUserVPNUnauthorized) Error() string {
	return fmt.Sprintf("[POST /user/vpn][%d] turnOnCurrentUserVpnUnauthorized ", 401)
}

func (o *TurnOnCurrentUserVPNUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewTurnOnCurrentUserVPNUnprocessableEntity creates a TurnOnCurrentUserVPNUnprocessableEntity with default headers values
func NewTurnOnCurrentUserVPNUnprocessableEntity() *TurnOnCurrentUserVPNUnprocessableEntity {
	return &TurnOnCurrentUserVPNUnprocessableEntity{}
}

/*TurnOnCurrentUserVPNUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type TurnOnCurrentUserVPNUnprocessableEntity struct {
}

func (o *TurnOnCurrentUserVPNUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /user/vpn][%d] turnOnCurrentUserVpnUnprocessableEntity ", 422)
}

func (o *TurnOnCurrentUserVPNUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
