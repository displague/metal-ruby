// Code generated by go-swagger; DO NOT EDIT.

package users

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindCurrentUserReader is a Reader for the FindCurrentUser structure.
type FindCurrentUserReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindCurrentUserReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindCurrentUserOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindCurrentUserUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindCurrentUserOK creates a FindCurrentUserOK with default headers values
func NewFindCurrentUserOK() *FindCurrentUserOK {
	return &FindCurrentUserOK{}
}

/*FindCurrentUserOK handles this case with default header values.

ok
*/
type FindCurrentUserOK struct {
	Payload *types.User
}

func (o *FindCurrentUserOK) Error() string {
	return fmt.Sprintf("[GET /user][%d] findCurrentUserOK  %+v", 200, o.Payload)
}

func (o *FindCurrentUserOK) GetPayload() *types.User {
	return o.Payload
}

func (o *FindCurrentUserOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.User)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindCurrentUserUnauthorized creates a FindCurrentUserUnauthorized with default headers values
func NewFindCurrentUserUnauthorized() *FindCurrentUserUnauthorized {
	return &FindCurrentUserUnauthorized{}
}

/*FindCurrentUserUnauthorized handles this case with default header values.

unauthorized
*/
type FindCurrentUserUnauthorized struct {
}

func (o *FindCurrentUserUnauthorized) Error() string {
	return fmt.Sprintf("[GET /user][%d] findCurrentUserUnauthorized ", 401)
}

func (o *FindCurrentUserUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
