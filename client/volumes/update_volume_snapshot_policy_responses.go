// Code generated by go-swagger; DO NOT EDIT.

package volumes

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// UpdateVolumeSnapshotPolicyReader is a Reader for the UpdateVolumeSnapshotPolicy structure.
type UpdateVolumeSnapshotPolicyReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *UpdateVolumeSnapshotPolicyReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewUpdateVolumeSnapshotPolicyOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewUpdateVolumeSnapshotPolicyUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewUpdateVolumeSnapshotPolicyForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewUpdateVolumeSnapshotPolicyNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewUpdateVolumeSnapshotPolicyUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewUpdateVolumeSnapshotPolicyOK creates a UpdateVolumeSnapshotPolicyOK with default headers values
func NewUpdateVolumeSnapshotPolicyOK() *UpdateVolumeSnapshotPolicyOK {
	return &UpdateVolumeSnapshotPolicyOK{}
}

/*UpdateVolumeSnapshotPolicyOK handles this case with default header values.

ok
*/
type UpdateVolumeSnapshotPolicyOK struct {
	Payload *types.SnapshotPolicy
}

func (o *UpdateVolumeSnapshotPolicyOK) Error() string {
	return fmt.Sprintf("[PUT /storage/snapshot-policies/{id}][%d] updateVolumeSnapshotPolicyOK  %+v", 200, o.Payload)
}

func (o *UpdateVolumeSnapshotPolicyOK) GetPayload() *types.SnapshotPolicy {
	return o.Payload
}

func (o *UpdateVolumeSnapshotPolicyOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.SnapshotPolicy)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateVolumeSnapshotPolicyUnauthorized creates a UpdateVolumeSnapshotPolicyUnauthorized with default headers values
func NewUpdateVolumeSnapshotPolicyUnauthorized() *UpdateVolumeSnapshotPolicyUnauthorized {
	return &UpdateVolumeSnapshotPolicyUnauthorized{}
}

/*UpdateVolumeSnapshotPolicyUnauthorized handles this case with default header values.

unauthorized
*/
type UpdateVolumeSnapshotPolicyUnauthorized struct {
}

func (o *UpdateVolumeSnapshotPolicyUnauthorized) Error() string {
	return fmt.Sprintf("[PUT /storage/snapshot-policies/{id}][%d] updateVolumeSnapshotPolicyUnauthorized ", 401)
}

func (o *UpdateVolumeSnapshotPolicyUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateVolumeSnapshotPolicyForbidden creates a UpdateVolumeSnapshotPolicyForbidden with default headers values
func NewUpdateVolumeSnapshotPolicyForbidden() *UpdateVolumeSnapshotPolicyForbidden {
	return &UpdateVolumeSnapshotPolicyForbidden{}
}

/*UpdateVolumeSnapshotPolicyForbidden handles this case with default header values.

forbidden
*/
type UpdateVolumeSnapshotPolicyForbidden struct {
}

func (o *UpdateVolumeSnapshotPolicyForbidden) Error() string {
	return fmt.Sprintf("[PUT /storage/snapshot-policies/{id}][%d] updateVolumeSnapshotPolicyForbidden ", 403)
}

func (o *UpdateVolumeSnapshotPolicyForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateVolumeSnapshotPolicyNotFound creates a UpdateVolumeSnapshotPolicyNotFound with default headers values
func NewUpdateVolumeSnapshotPolicyNotFound() *UpdateVolumeSnapshotPolicyNotFound {
	return &UpdateVolumeSnapshotPolicyNotFound{}
}

/*UpdateVolumeSnapshotPolicyNotFound handles this case with default header values.

not found
*/
type UpdateVolumeSnapshotPolicyNotFound struct {
}

func (o *UpdateVolumeSnapshotPolicyNotFound) Error() string {
	return fmt.Sprintf("[PUT /storage/snapshot-policies/{id}][%d] updateVolumeSnapshotPolicyNotFound ", 404)
}

func (o *UpdateVolumeSnapshotPolicyNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateVolumeSnapshotPolicyUnprocessableEntity creates a UpdateVolumeSnapshotPolicyUnprocessableEntity with default headers values
func NewUpdateVolumeSnapshotPolicyUnprocessableEntity() *UpdateVolumeSnapshotPolicyUnprocessableEntity {
	return &UpdateVolumeSnapshotPolicyUnprocessableEntity{}
}

/*UpdateVolumeSnapshotPolicyUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type UpdateVolumeSnapshotPolicyUnprocessableEntity struct {
}

func (o *UpdateVolumeSnapshotPolicyUnprocessableEntity) Error() string {
	return fmt.Sprintf("[PUT /storage/snapshot-policies/{id}][%d] updateVolumeSnapshotPolicyUnprocessableEntity ", 422)
}

func (o *UpdateVolumeSnapshotPolicyUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
