// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// UpdateProjectReader is a Reader for the UpdateProject structure.
type UpdateProjectReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *UpdateProjectReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewUpdateProjectOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewUpdateProjectUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewUpdateProjectForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewUpdateProjectNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewUpdateProjectUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewUpdateProjectOK creates a UpdateProjectOK with default headers values
func NewUpdateProjectOK() *UpdateProjectOK {
	return &UpdateProjectOK{}
}

/*UpdateProjectOK handles this case with default header values.

ok
*/
type UpdateProjectOK struct {
	Payload *models.Project
}

func (o *UpdateProjectOK) Error() string {
	return fmt.Sprintf("[PUT /projects/{id}][%d] updateProjectOK  %+v", 200, o.Payload)
}

func (o *UpdateProjectOK) GetPayload() *models.Project {
	return o.Payload
}

func (o *UpdateProjectOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.Project)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateProjectUnauthorized creates a UpdateProjectUnauthorized with default headers values
func NewUpdateProjectUnauthorized() *UpdateProjectUnauthorized {
	return &UpdateProjectUnauthorized{}
}

/*UpdateProjectUnauthorized handles this case with default header values.

unauthorized
*/
type UpdateProjectUnauthorized struct {
}

func (o *UpdateProjectUnauthorized) Error() string {
	return fmt.Sprintf("[PUT /projects/{id}][%d] updateProjectUnauthorized ", 401)
}

func (o *UpdateProjectUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateProjectForbidden creates a UpdateProjectForbidden with default headers values
func NewUpdateProjectForbidden() *UpdateProjectForbidden {
	return &UpdateProjectForbidden{}
}

/*UpdateProjectForbidden handles this case with default header values.

forbidden
*/
type UpdateProjectForbidden struct {
}

func (o *UpdateProjectForbidden) Error() string {
	return fmt.Sprintf("[PUT /projects/{id}][%d] updateProjectForbidden ", 403)
}

func (o *UpdateProjectForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateProjectNotFound creates a UpdateProjectNotFound with default headers values
func NewUpdateProjectNotFound() *UpdateProjectNotFound {
	return &UpdateProjectNotFound{}
}

/*UpdateProjectNotFound handles this case with default header values.

not found
*/
type UpdateProjectNotFound struct {
}

func (o *UpdateProjectNotFound) Error() string {
	return fmt.Sprintf("[PUT /projects/{id}][%d] updateProjectNotFound ", 404)
}

func (o *UpdateProjectNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateProjectUnprocessableEntity creates a UpdateProjectUnprocessableEntity with default headers values
func NewUpdateProjectUnprocessableEntity() *UpdateProjectUnprocessableEntity {
	return &UpdateProjectUnprocessableEntity{}
}

/*UpdateProjectUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type UpdateProjectUnprocessableEntity struct {
}

func (o *UpdateProjectUnprocessableEntity) Error() string {
	return fmt.Sprintf("[PUT /projects/{id}][%d] updateProjectUnprocessableEntity ", 422)
}

func (o *UpdateProjectUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}