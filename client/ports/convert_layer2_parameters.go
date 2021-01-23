// Code generated by go-swagger; DO NOT EDIT.

package ports

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// NewConvertLayer2Params creates a new ConvertLayer2Params object
// with the default values initialized.
func NewConvertLayer2Params() *ConvertLayer2Params {
	var ()
	return &ConvertLayer2Params{

		timeout: cr.DefaultTimeout,
	}
}

// NewConvertLayer2ParamsWithTimeout creates a new ConvertLayer2Params object
// with the default values initialized, and the ability to set a timeout on a request
func NewConvertLayer2ParamsWithTimeout(timeout time.Duration) *ConvertLayer2Params {
	var ()
	return &ConvertLayer2Params{

		timeout: timeout,
	}
}

// NewConvertLayer2ParamsWithContext creates a new ConvertLayer2Params object
// with the default values initialized, and the ability to set a context for a request
func NewConvertLayer2ParamsWithContext(ctx context.Context) *ConvertLayer2Params {
	var ()
	return &ConvertLayer2Params{

		Context: ctx,
	}
}

// NewConvertLayer2ParamsWithHTTPClient creates a new ConvertLayer2Params object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewConvertLayer2ParamsWithHTTPClient(client *http.Client) *ConvertLayer2Params {
	var ()
	return &ConvertLayer2Params{
		HTTPClient: client,
	}
}

/*ConvertLayer2Params contains all the parameters to send to the API endpoint
for the convert layer2 operation typically these are written to a http.Request
*/
type ConvertLayer2Params struct {

	/*ID
	  Port UUID

	*/
	ID strfmt.UUID
	/*Vnid
	  Virtual Network ID

	*/
	Vnid *types.PortAssignInput

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the convert layer2 params
func (o *ConvertLayer2Params) WithTimeout(timeout time.Duration) *ConvertLayer2Params {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the convert layer2 params
func (o *ConvertLayer2Params) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the convert layer2 params
func (o *ConvertLayer2Params) WithContext(ctx context.Context) *ConvertLayer2Params {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the convert layer2 params
func (o *ConvertLayer2Params) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the convert layer2 params
func (o *ConvertLayer2Params) WithHTTPClient(client *http.Client) *ConvertLayer2Params {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the convert layer2 params
func (o *ConvertLayer2Params) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the convert layer2 params
func (o *ConvertLayer2Params) WithID(id strfmt.UUID) *ConvertLayer2Params {
	o.SetID(id)
	return o
}

// SetID adds the id to the convert layer2 params
func (o *ConvertLayer2Params) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithVnid adds the vnid to the convert layer2 params
func (o *ConvertLayer2Params) WithVnid(vnid *types.PortAssignInput) *ConvertLayer2Params {
	o.SetVnid(vnid)
	return o
}

// SetVnid adds the vnid to the convert layer2 params
func (o *ConvertLayer2Params) SetVnid(vnid *types.PortAssignInput) {
	o.Vnid = vnid
}

// WriteToRequest writes these params to a swagger request
func (o *ConvertLayer2Params) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Vnid != nil {
		if err := r.SetBodyParam(o.Vnid); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
