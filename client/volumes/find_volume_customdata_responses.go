// Code generated by go-swagger; DO NOT EDIT.

package volumes

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// FindVolumeCustomdataReader is a Reader for the FindVolumeCustomdata structure.
type FindVolumeCustomdataReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindVolumeCustomdataReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindVolumeCustomdataOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindVolumeCustomdataUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewFindVolumeCustomdataForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewFindVolumeCustomdataNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindVolumeCustomdataOK creates a FindVolumeCustomdataOK with default headers values
func NewFindVolumeCustomdataOK() *FindVolumeCustomdataOK {
	return &FindVolumeCustomdataOK{}
}

/*FindVolumeCustomdataOK handles this case with default header values.

ok
*/
type FindVolumeCustomdataOK struct {
}

func (o *FindVolumeCustomdataOK) Error() string {
	return fmt.Sprintf("[GET /storage/{id}/customdata][%d] findVolumeCustomdataOK ", 200)
}

func (o *FindVolumeCustomdataOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindVolumeCustomdataUnauthorized creates a FindVolumeCustomdataUnauthorized with default headers values
func NewFindVolumeCustomdataUnauthorized() *FindVolumeCustomdataUnauthorized {
	return &FindVolumeCustomdataUnauthorized{}
}

/*FindVolumeCustomdataUnauthorized handles this case with default header values.

unauthorized
*/
type FindVolumeCustomdataUnauthorized struct {
}

func (o *FindVolumeCustomdataUnauthorized) Error() string {
	return fmt.Sprintf("[GET /storage/{id}/customdata][%d] findVolumeCustomdataUnauthorized ", 401)
}

func (o *FindVolumeCustomdataUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindVolumeCustomdataForbidden creates a FindVolumeCustomdataForbidden with default headers values
func NewFindVolumeCustomdataForbidden() *FindVolumeCustomdataForbidden {
	return &FindVolumeCustomdataForbidden{}
}

/*FindVolumeCustomdataForbidden handles this case with default header values.

forbidden
*/
type FindVolumeCustomdataForbidden struct {
}

func (o *FindVolumeCustomdataForbidden) Error() string {
	return fmt.Sprintf("[GET /storage/{id}/customdata][%d] findVolumeCustomdataForbidden ", 403)
}

func (o *FindVolumeCustomdataForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewFindVolumeCustomdataNotFound creates a FindVolumeCustomdataNotFound with default headers values
func NewFindVolumeCustomdataNotFound() *FindVolumeCustomdataNotFound {
	return &FindVolumeCustomdataNotFound{}
}

/*FindVolumeCustomdataNotFound handles this case with default header values.

not found
*/
type FindVolumeCustomdataNotFound struct {
}

func (o *FindVolumeCustomdataNotFound) Error() string {
	return fmt.Sprintf("[GET /storage/{id}/customdata][%d] findVolumeCustomdataNotFound ", 404)
}

func (o *FindVolumeCustomdataNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
