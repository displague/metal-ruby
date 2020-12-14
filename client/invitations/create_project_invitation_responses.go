// Code generated by go-swagger; DO NOT EDIT.

package invitations

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// CreateProjectInvitationReader is a Reader for the CreateProjectInvitation structure.
type CreateProjectInvitationReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CreateProjectInvitationReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewCreateProjectInvitationCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewCreateProjectInvitationUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewCreateProjectInvitationForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCreateProjectInvitationNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewCreateProjectInvitationUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewCreateProjectInvitationCreated creates a CreateProjectInvitationCreated with default headers values
func NewCreateProjectInvitationCreated() *CreateProjectInvitationCreated {
	return &CreateProjectInvitationCreated{}
}

/*CreateProjectInvitationCreated handles this case with default header values.

created
*/
type CreateProjectInvitationCreated struct {
	Payload *models.Invitation
}

func (o *CreateProjectInvitationCreated) Error() string {
	return fmt.Sprintf("[POST /projects/{project_id}/invitations][%d] createProjectInvitationCreated  %+v", 201, o.Payload)
}

func (o *CreateProjectInvitationCreated) GetPayload() *models.Invitation {
	return o.Payload
}

func (o *CreateProjectInvitationCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.Invitation)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCreateProjectInvitationUnauthorized creates a CreateProjectInvitationUnauthorized with default headers values
func NewCreateProjectInvitationUnauthorized() *CreateProjectInvitationUnauthorized {
	return &CreateProjectInvitationUnauthorized{}
}

/*CreateProjectInvitationUnauthorized handles this case with default header values.

unauthorized
*/
type CreateProjectInvitationUnauthorized struct {
}

func (o *CreateProjectInvitationUnauthorized) Error() string {
	return fmt.Sprintf("[POST /projects/{project_id}/invitations][%d] createProjectInvitationUnauthorized ", 401)
}

func (o *CreateProjectInvitationUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateProjectInvitationForbidden creates a CreateProjectInvitationForbidden with default headers values
func NewCreateProjectInvitationForbidden() *CreateProjectInvitationForbidden {
	return &CreateProjectInvitationForbidden{}
}

/*CreateProjectInvitationForbidden handles this case with default header values.

forbidden
*/
type CreateProjectInvitationForbidden struct {
}

func (o *CreateProjectInvitationForbidden) Error() string {
	return fmt.Sprintf("[POST /projects/{project_id}/invitations][%d] createProjectInvitationForbidden ", 403)
}

func (o *CreateProjectInvitationForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateProjectInvitationNotFound creates a CreateProjectInvitationNotFound with default headers values
func NewCreateProjectInvitationNotFound() *CreateProjectInvitationNotFound {
	return &CreateProjectInvitationNotFound{}
}

/*CreateProjectInvitationNotFound handles this case with default header values.

not found
*/
type CreateProjectInvitationNotFound struct {
}

func (o *CreateProjectInvitationNotFound) Error() string {
	return fmt.Sprintf("[POST /projects/{project_id}/invitations][%d] createProjectInvitationNotFound ", 404)
}

func (o *CreateProjectInvitationNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateProjectInvitationUnprocessableEntity creates a CreateProjectInvitationUnprocessableEntity with default headers values
func NewCreateProjectInvitationUnprocessableEntity() *CreateProjectInvitationUnprocessableEntity {
	return &CreateProjectInvitationUnprocessableEntity{}
}

/*CreateProjectInvitationUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type CreateProjectInvitationUnprocessableEntity struct {
}

func (o *CreateProjectInvitationUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /projects/{project_id}/invitations][%d] createProjectInvitationUnprocessableEntity ", 422)
}

func (o *CreateProjectInvitationUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}