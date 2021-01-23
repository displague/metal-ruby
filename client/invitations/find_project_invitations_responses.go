// Code generated by go-swagger; DO NOT EDIT.

package invitations

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindProjectInvitationsReader is a Reader for the FindProjectInvitations structure.
type FindProjectInvitationsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindProjectInvitationsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindProjectInvitationsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindProjectInvitationsUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindProjectInvitationsForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindProjectInvitationsNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindProjectInvitationsOK creates a FindProjectInvitationsOK with default headers values
func NewFindProjectInvitationsOK() *FindProjectInvitationsOK {
	return &FindProjectInvitationsOK{}
}

/*FindProjectInvitationsOK handles this case with default header values.

ok
*/
type FindProjectInvitationsOK struct {
	Payload *types.InvitationList
}

func (o *FindProjectInvitationsOK) Error() string {
	return fmt.Sprintf("[GET /projects/{project_id}/invitations][%d] findProjectInvitationsOK  %+v", 200, o.Payload)
}

func (o *FindProjectInvitationsOK) GetPayload() *types.InvitationList {
	return o.Payload
}

func (o *FindProjectInvitationsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.InvitationList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindProjectInvitationsUnauthorized creates a FindProjectInvitationsUnauthorized with default headers values
func NewFindProjectInvitationsUnauthorized() *FindProjectInvitationsUnauthorized {
	return &FindProjectInvitationsUnauthorized{}
}

/*FindProjectInvitationsUnauthorized handles this case with default header values.

unauthorized
*/
type FindProjectInvitationsUnauthorized struct {
}

func (o *FindProjectInvitationsUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{project_id}/invitations][%d] findProjectInvitationsUnauthorized ", 401)
}

func (o *FindProjectInvitationsUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectInvitationsForbidden creates a FindProjectInvitationsForbidden with default headers values
func NewFindProjectInvitationsForbidden() *FindProjectInvitationsForbidden {
	return &FindProjectInvitationsForbidden{}
}

/*FindProjectInvitationsForbidden handles this case with default header values.

forbidden
*/
type FindProjectInvitationsForbidden struct {
}

func (o *FindProjectInvitationsForbidden) Error() string {
	return fmt.Sprintf("[GET /projects/{project_id}/invitations][%d] findProjectInvitationsForbidden ", 403)
}

func (o *FindProjectInvitationsForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectInvitationsNotFound creates a FindProjectInvitationsNotFound with default headers values
func NewFindProjectInvitationsNotFound() *FindProjectInvitationsNotFound {
	return &FindProjectInvitationsNotFound{}
}

/*FindProjectInvitationsNotFound handles this case with default header values.

not found
*/
type FindProjectInvitationsNotFound struct {
}

func (o *FindProjectInvitationsNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{project_id}/invitations][%d] findProjectInvitationsNotFound ", 404)
}

func (o *FindProjectInvitationsNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
