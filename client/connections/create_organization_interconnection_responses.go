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

// CreateOrganizationInterconnectionReader is a Reader for the CreateOrganizationInterconnection structure.
type CreateOrganizationInterconnectionReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CreateOrganizationInterconnectionReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewCreateOrganizationInterconnectionCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewCreateOrganizationInterconnectionForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCreateOrganizationInterconnectionNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewCreateOrganizationInterconnectionCreated creates a CreateOrganizationInterconnectionCreated with default headers values
func NewCreateOrganizationInterconnectionCreated() *CreateOrganizationInterconnectionCreated {
	return &CreateOrganizationInterconnectionCreated{}
}

/*CreateOrganizationInterconnectionCreated handles this case with default header values.

created
*/
type CreateOrganizationInterconnectionCreated struct {
	Payload *types.Interconnection
}

func (o *CreateOrganizationInterconnectionCreated) Error() string {
	return fmt.Sprintf("[POST /organizations/{organization_id}/connections][%d] createOrganizationInterconnectionCreated  %+v", 201, o.Payload)
}

func (o *CreateOrganizationInterconnectionCreated) GetPayload() *types.Interconnection {
	return o.Payload
}

func (o *CreateOrganizationInterconnectionCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.Interconnection)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCreateOrganizationInterconnectionForbidden creates a CreateOrganizationInterconnectionForbidden with default headers values
func NewCreateOrganizationInterconnectionForbidden() *CreateOrganizationInterconnectionForbidden {
	return &CreateOrganizationInterconnectionForbidden{}
}

/*CreateOrganizationInterconnectionForbidden handles this case with default header values.

forbidden
*/
type CreateOrganizationInterconnectionForbidden struct {
}

func (o *CreateOrganizationInterconnectionForbidden) Error() string {
	return fmt.Sprintf("[POST /organizations/{organization_id}/connections][%d] createOrganizationInterconnectionForbidden ", 403)
}

func (o *CreateOrganizationInterconnectionForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateOrganizationInterconnectionNotFound creates a CreateOrganizationInterconnectionNotFound with default headers values
func NewCreateOrganizationInterconnectionNotFound() *CreateOrganizationInterconnectionNotFound {
	return &CreateOrganizationInterconnectionNotFound{}
}

/*CreateOrganizationInterconnectionNotFound handles this case with default header values.

not found
*/
type CreateOrganizationInterconnectionNotFound struct {
}

func (o *CreateOrganizationInterconnectionNotFound) Error() string {
	return fmt.Sprintf("[POST /organizations/{organization_id}/connections][%d] createOrganizationInterconnectionNotFound ", 404)
}

func (o *CreateOrganizationInterconnectionNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
