// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// FindProjectLicensesReader is a Reader for the FindProjectLicenses structure.
type FindProjectLicensesReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindProjectLicensesReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindProjectLicensesOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindProjectLicensesUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindProjectLicensesForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindProjectLicensesNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindProjectLicensesOK creates a FindProjectLicensesOK with default headers values
func NewFindProjectLicensesOK() *FindProjectLicensesOK {
	return &FindProjectLicensesOK{}
}

/*FindProjectLicensesOK handles this case with default header values.

ok
*/
type FindProjectLicensesOK struct {
	Payload *types.LicenseList
}

func (o *FindProjectLicensesOK) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/licenses][%d] findProjectLicensesOK  %+v", 200, o.Payload)
}

func (o *FindProjectLicensesOK) GetPayload() *types.LicenseList {
	return o.Payload
}

func (o *FindProjectLicensesOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(types.LicenseList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindProjectLicensesUnauthorized creates a FindProjectLicensesUnauthorized with default headers values
func NewFindProjectLicensesUnauthorized() *FindProjectLicensesUnauthorized {
	return &FindProjectLicensesUnauthorized{}
}

/*FindProjectLicensesUnauthorized handles this case with default header values.

unauthorized
*/
type FindProjectLicensesUnauthorized struct {
}

func (o *FindProjectLicensesUnauthorized) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/licenses][%d] findProjectLicensesUnauthorized ", 401)
}

func (o *FindProjectLicensesUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectLicensesForbidden creates a FindProjectLicensesForbidden with default headers values
func NewFindProjectLicensesForbidden() *FindProjectLicensesForbidden {
	return &FindProjectLicensesForbidden{}
}

/*FindProjectLicensesForbidden handles this case with default header values.

forbidden
*/
type FindProjectLicensesForbidden struct {
}

func (o *FindProjectLicensesForbidden) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/licenses][%d] findProjectLicensesForbidden ", 403)
}

func (o *FindProjectLicensesForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindProjectLicensesNotFound creates a FindProjectLicensesNotFound with default headers values
func NewFindProjectLicensesNotFound() *FindProjectLicensesNotFound {
	return &FindProjectLicensesNotFound{}
}

/*FindProjectLicensesNotFound handles this case with default header values.

not found
*/
type FindProjectLicensesNotFound struct {
}

func (o *FindProjectLicensesNotFound) Error() string {
	return fmt.Sprintf("[GET /projects/{id}/licenses][%d] findProjectLicensesNotFound ", 404)
}

func (o *FindProjectLicensesNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
