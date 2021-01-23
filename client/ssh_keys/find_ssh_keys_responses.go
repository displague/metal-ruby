// Code generated by go-swagger; DO NOT EDIT.

package ssh_keys

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindSSHKeysReader is a Reader for the FindSSHKeys structure.
type FindSSHKeysReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindSSHKeysReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindSSHKeysOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindSSHKeysUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindSSHKeysOK creates a FindSSHKeysOK with default headers values
func NewFindSSHKeysOK() *FindSSHKeysOK {
	return &FindSSHKeysOK{}
}

/*FindSSHKeysOK handles this case with default header values.

ok
*/
type FindSSHKeysOK struct {
	Payload *types.SSHKeyList
}

func (o *FindSSHKeysOK) Error() string {
	return fmt.Sprintf("[GET /ssh-keys][%d] findSshKeysOK  %+v", 200, o.Payload)
}

func (o *FindSSHKeysOK) GetPayload() *types.SSHKeyList {
	return o.Payload
}

func (o *FindSSHKeysOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.SSHKeyList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindSSHKeysUnauthorized creates a FindSSHKeysUnauthorized with default headers values
func NewFindSSHKeysUnauthorized() *FindSSHKeysUnauthorized {
	return &FindSSHKeysUnauthorized{}
}

/*FindSSHKeysUnauthorized handles this case with default header values.

unauthorized
*/
type FindSSHKeysUnauthorized struct {
}

func (o *FindSSHKeysUnauthorized) Error() string {
	return fmt.Sprintf("[GET /ssh-keys][%d] findSshKeysUnauthorized ", 401)
}

func (o *FindSSHKeysUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
